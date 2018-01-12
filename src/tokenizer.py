# file:         tokenizer.py
# date:         21.12.2017
# author:       Peter Sprenger
# description:  This script will tokenize the data set and filter out function
#               words that we don't want to have in the topic models.

# Import necessary modules.
import sys, os
from nltk import wordpunct_tokenize as tokenizer
#from nltk.stem import PorterStemmer
#from nltk.stem.isri import ISRIStemmer
from nltk.corpus import stopwords

# Take sys.argv[1] as input which language function should be run.
language = sys.argv[1]

def en():
    # Take sys.argv[2] as input which data set should be run.
    # Create a list of the files in the chosen directory.
    directory = sys.argv[2]
    files = os.listdir("../out/" + directory + "/en/")

    # Create counter, set to zero.
    counter = 0

    # Import stop words.
    sw_en = stopwords.words('english')

    # DELETE THIS Import Porterstemmer()
    # st = PorterStemmer()

    # Loop over files:
    for f in files:
        counter += 1
        print("Beginning file: " + str(counter))
        allwords = []

        if "txt" in f:
            # Open and read in file.
            f_in = open("../out/" + directory + "/en/" + f, 'rU')
            lines = f_in.readlines()
            f_in.close()

            # Loop over the lines in the opened file:
            # lowercase and tokenize words.
            for line in lines:
                words = []
                line = line.lower()
                tokens = tokenizer(line)

                # Loop over the words in tokens:
                # pass if the word is in the list of stop words.
                # all other words: stem the word (???) and append to list: words.
                for t in tokens:
                    try:
                        if t in sw_en:
                            pass
                        else:
                            words.append(t)
                    except IndexError:
                        words.append(t)

            allwords.append(words)

            # Write the stemmed words to file.
            f_out = open("../out/tokenized/" + directory + "/en/" + f, 'w')
            for item in allwords:
                f_out.write("\n".join(item))
            f_out.close()


def ar():
    # Take sys.argv[2] as input which data set should be run.
    # Create a list of the files in the chosen directory.
    directory = sys.argv[2]
    files = os.listdir("../out/" + directory + "/ar/")

    # Create counter, set to zero.
    counter = 0

    # Open file with Arabic stop words.
    sw_in = open("../data/arstoplist.txt")
    sw = sw_in.read().splitlines()
    sw_in.close()

    # Open file with Arabic punctuation.
    punctlist = open("../data/arabpunct.txt").read().splitlines()

    # DELETE THIS Import IsriStemmer() 
    # st = ISRIStemmer()

    # Loop over files:
    for f in files:
        counter += 1
        print("Beginning file: " + str(counter))
        allwords = []

        if "txt" in f:
            # Open and read in file.
            f_in = open("../out/" + directory + "/ar/" + f, 'rU')
            lines = f_in.readlines()
            f_in.close()

            # Loop over the lines in the file.
            for line in lines:
                words = []

                # Tokenize the line.
                tokens = tokenizer(line)

                # Loop over the words in the line:
                # Pass if the word appears in the stopwords or punctuation list.
                # Stem all other tokens and append to: words.
                for t in tokens:
                    if t in sw:
                        pass
                    elif t in punctlist:
                        pass
                    else:
                        words.append(t) # Why stem here???!!!


                allwords.append(words)


            # Write stemmed words to file.
            f_out = open("../out/tokenized/" + directory + "/ar/" + f, 'w')
            for item in allwords:
                f_out.write("\n".join(item))
            f_out.close()

if language == "en":
	en()
elif language == "ar":
	ar()
