# test3.py
# author: Peter Sprenger
# date: 06.08.2017

"""
get root for each word in topic modeling output.
check how many words have the same root (as the top word?).
calculate as follows: 1 divided by number of roots
A A A B C D = score of 0.25
A A A B B B = score of 0.5
"""


import sys, os, re
from nltk import wordpunct_tokenize as tokenizer
from nltk.stem.isri import ISRIStemmer
import numpy as np
import collections
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
#import math





def main():
    corpora = sys.argv[1]
    topics = sys.argv[2]
    topwords = sys.argv[3]

    st = ISRIStemmer()

    f_in = open("../out/mallet/test/" + corpora + "-" + topics + "-" + topwords + ".txt")
    f = f_in.readlines()
    f_in.close()

    words = []
    stemlist = []

    for line in f:
        line = tokenizer(line)
        del line[0:4]
        words.append(line)

    for listitem in words:

        stems = []

        for w in listitem:
            r = st.stem(w)
            stems.append(r)

        stemlist.append(stems)

    sorted_by_rank = []

    for i in range(10):
        possort = []
        for l in stemlist:
            possort.append(l[i])
        sorted_by_rank.append(possort)

    lcount = []
    dcount = []

    for i in sorted_by_rank:
        l = []
        d = {}
        for w in i:
            if w in d:
                d[w] += 1
                l.append(0)
            else:
                d[w] = 1
                l.append(1)
        dcount.append(d)
        lcount.append(l)



    c1 = -1

    plotdata = []

    for l in sorted_by_rank:
        c1 += 1
        c2 = -1
        plotdata_sub = []

        for word in l:
            c2 += 1
            if lcount[c1][c2] == 1:
                plotdata_sub.append(dcount[c1].get(word))
            else:
                pass

        plotdata.append(plotdata_sub)


    fig = plt.figure(1, figsize=(9, 6))

    ax = fig.add_subplot(111)

    bp = ax.boxplot(plotdata)#, showbox=False, showcaps=False)

    ax.set_xticklabels(['#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9', '#10'])

    #ax.set_yscale('log')

    ax.set_yticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    ax.set_ylabel("Number of repetition", rotation='vertical')
    ax.set_xlabel("Rank in topic model output")
    ax.set_title("UN 50 topics")

    fig.savefig('../out/mallet/figures/un-50.png', bbox_inches='tight')
    #plt.show()

main()
