# test2.py
# author: Peter Sprenger
# date: 31.10.2017

# Import necessary modules.
import sys
from nltk import wordpunct_tokenize as tokenizer
from nltk.stem.isri import ISRIStemmer
import numpy as np
import matplotlib.pyplot as plt

# For proper display of LaTeX default font
from matplotlib import rc
rc('font',**{'family':'serif','sans-serif':['Computer Modern Roman']})
rc('text', usetex=True)


def main():

    # Define which corpora to work with via sys.argv[1]
    corpora = sys.argv[1]

    # Define input data.
    k50 = "../out/mallet/testdez/" + corpora + "-50.txt"
    k100 = "../out/mallet/testdez/" + corpora + "-100.txt"
    k200 = "../out/mallet/testdez/" + corpora + "-200.txt"

    # Load ISRIStemmer.
    st = ISRIStemmer()

    # Create lists: all_plots, all_means.
    all_plots = []
    all_means = []

    # Create for loop over the three files.
    for i in (k50, k100, k200):
        # Open file, read it into variable f, close file.
        f_in = open(i)
        f = f_in.readlines()
        f_in.close()

        # Create lists: words, stemlist.
        words = []
        stemlist = []

        # Loop over the lines in f. Tokenize words, delete the numbers at the
        # beginning of each line (0:4). Append line to words.
        for line in f:
            line = tokenizer(line)
            del line[0:4]
            words.append(line)

        # Loop over words. Stem each word and append to stemlist.
        for listitem in words:
            stems = []
            for w in listitem:
                r = st.stem(w)
                stems.append(r)
            stemlist.append(stems)

        # Create lists: score, plotdata.
        score = []
        plotdata = []

        # Loop over lists in stemlist. Create a dictionary: d.
        # Loop over the words in topic:
        # if word is in d: add 1 to its value in d.
        # else: add word to d.
        for topic in stemlist:
            d = {}
            for item in topic:
                if item in d:
                    d[item] += 1
                else:
                    d[item] = 1

            # Get the value of each word in d and append it to plotdata.
            maximum = max(d, key=d.get)
            plotdata.append(d[maximum])

            # Calculate the score: 1 / len(d).
            # Append each d_score to score.
            d_score = 1 / len(d)
            score.append(d_score)

        # Calculate the mean of score. Append to all_means.
        mean = np.mean(score)
        all_means.append(mean)

        # Append plotdata to all_plots.
        all_plots.append(plotdata)
        print(plotdata)

    # Create figure: boxplot with data from "all_plots".
    xtick50 = "k=50, mean score over \n all topics: "+ str(round(all_means[0], 4))
    xtick100 = "k=100, mean score over \n all topics: "+ str(round(all_means[1], 4))
    xtick200 = "k=200, mean score over \n all topics: "+ str(round(all_means[2], 4))
    fig = plt.figure(1, figsize=(9, 6))
    ax = fig.add_subplot(111)
    ax.boxplot(all_plots)
    ax.set_xticklabels([xtick50, xtick100, xtick200])
    ax.set_yticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    ax.set_ylabel("Highest value of root repetition per topic", rotation='vertical')
    ax.set_xlabel("k = topics")
    ax.set_title("UN")
    fig.savefig('../out/mallet/figures/testdez/un.png', bbox_inches='tight')
    #plt.show()

main()
