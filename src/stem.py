# stem.py
# author: Peter Sprenger
# date: 02.06.2017
# This script takes the input file, stems the Arabic text using ISRIStemmer and saves the output in a new file (not done yet).
import sys, os, re
#from nltk import word_tokenize # doesn't work well
from nltk import wordpunct_tokenize as tokenizer #works apparently better. will be used from now on.
from nltk.stem.isri import ISRIStemmer
from collections import Counter
#from unicodedata import normalize # wird doch nicht benutzt.

def main():

    # Open all files related to removing stop words or punctuation from the data.
    sw_in = open(r"../data/arstoplist.txt")
    stopwords = sw_in.read().splitlines()
    punctlist = open("../data/arabpunct.txt").read().splitlines()

    directory = sys.argv[1]

    # Give location of input files.
    files = os.listdir("../out/" + directory + "/ar/")

    st = ISRIStemmer()
    #rx_en = re.compile(r'\D+')
    tokens = []
    counter = 0
    filelist = []

    for f in files:
        if "txt" in f:
            counter += 1
            f_in = open("../out/" + directory + "/ar/" + f, 'rU')
            lines = f_in.readlines()
            f_in.close()
            filelist.extend(lines)

    print("Files read.")

    stemmed = {}
    types = {}

    f_out = open('../out/testset-tokenized-' + directory + '.txt', 'w')
    compl_list = []

    for line in filelist:
        #line = line.strip()
        #tokenize = word_tokenize(line)

        # Tokenize the text.
        tokenize = tokenizer(line)

        #tokenize.sort() # Comment this out after the test-set has been used?

        # Define all patterns that shall be excluded.
        rx_ar = re.compile(u'^[\u0621-\u064A]+$') # This exludes Arabic words that have numbers attached to them.
        rx_ar2 = re.compile(u'^(\u0622{2,})')

        for w in tokenize:
            if len(w) == 1:
                pass
            elif rx_ar2.match(w):
                pass
            elif rx_ar.match(w):
                f_out.write(w + "\n")
                compl_list.append(w)
            else:
                pass
    f_out.close()

    # wieder einfügen

    for w in compl_list:
        types[w] = 0
        #if punctlist[0] in compl_list or punctlist[1] in compl_list or punctlist[2] or punctlist[3] in compl_list:
        #    if len(w) > 1: # ERROR
        #        new_w = w[:-1] # ERROR! This strips off Arabic letters although they are not in the punctlist
        #        types[new_w] = 0
        #        tokens.append(new_w)
        #    else:
        #        types[w] = 0
        #        tokens.append(w)

    print(str(len(types)) + " different words.")
    print("Punctuation separated.")

    # Here the actual stemming happens.
    verbs = {}
    c = -1
    for w in types:
        c +=1
        if w not in stopwords:
            stm = st.stem(w)
            stemmed[w] = stm
            verbs[stm] = 0
        if c % 10000 == 0:
            print(str(c) + " words stemmed.")
    print("File stemmed.")

    # print the stemmed words and their unstemmed versions to a file
    f_out = open('../out/stem_tok_' + directory + '.txt', 'w')
    wordlist = []
    for w in verbs.keys():
        if len(w) > 4: # Don't save words that are longer than 4 letters. Verbs in Arabic are usually 3 letters long. Ivery rare cases they can be 2 or 4 letters long as well.
            pass
        else:
            wordlist.append(w)
            #f_out.write(w + "\t" + stemmed[w])
            #f_out.write(w + "\n")
    wordlist.sort()
    for w in wordlist:
            f_out.write(w + "\n")
    f_out.write("No. of verbs:" + str(len(wordlist))) # Really verbs? Why not wordlist?
    f_out.close()

    # handle some corpora stats
    corp_stat = Counter(tokens)
    for w in list(corp_stat.keys())[0:11]:
        print("token: " + w + "\tno.: " + str(corp_stat[w]))

main()
