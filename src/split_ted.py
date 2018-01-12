# file: 	   split_ted.py
# author:      Peter Sprenger
# date:        29.05.2017
# description: Extract all English and all Arabic lines from the
# 			   TED talk subtitle data set and put them in
# 			   separate txt files, sorted by resolutions.


# Import necessary modules.
import sys, re

# Set sys.argv[1] as language - en/ar as options.
language = sys.argv[1]

# Function that will split the English text.
def en():
	# Open and read in the file.
	f_in = open("../data/ted/ar-en-ted.tmx", 'rU')
	lines = f_in.readlines()
	f_in.close()

	# RegEx that will match English lines.
	rx_en = re.compile('<tuv xml:lang="en">')

    # RegEx that will match the lines with the numbers of the talks.
	rx_en2 = re.compile('<tuv xml:lang="en"><seg>\d+</seg></tuv>')

    # RegEx that will match the line with the link to the talk.
	rx_http_en = re.compile('<tuv xml:lang="en"><seg>http://www.ted.com/talks/')

	# Create variable that will store the resolutions: en.
	en = []

	# Create counter_en, set to zero.
	counter_en = 0

	# Create variable num to store the file name.
	num = None

	# Create for loop over "lines".
	for line in lines:
        # Strip off whitespace.
		line = line.strip()

        # If http-RegEx matches the line
        # and counter_en is > 0:
        # delete metadata from en,
        # save en to file;
        # reset en.
		if rx_http_en.match(line):
			if counter_en > 0:
				del en[0:4]
				f_out_en = open("../out/ted/en/" + str(num) + "en.txt", 'w')
				str_en = '\n'.join(en)
				str_en = re.sub(r"\n", " ", str_en)
				f_out_en.write(str_en)
				en = []

		else:
            # If RegEx matches the line with the number,
            # delete XML and save no to variable: num.
            # Add 1 to counter_en.
            # If RegEx matches a regular line:
            # delete XML, append line to en.
			if rx_en2.match(line):
				num = re.sub(r"</?[^>]*>","", line)
				#print("num", num)
				counter_en += 1
			if rx_en.match(line):
				line = re.sub(r"</seg></tuv>", " ", str(line))
				line = re.sub(r"<tuv xml:lang=\"en\"><seg>", "", line)
				en.append(line)

    # If there is data left in en:
    # get the number of the talk from en: num,
    # delete metadata; save en to file.
	if en:
		num = en[2]
		del en[0:4]
		f_out_en = open("../out/ted/en/" + str(num) + "en.txt", 'w')
		str_en = '\n'.join(en)
		str_en = re.sub(r"\n", " ", str_en)
		f_out_en.write(str_en)



# Function that will split the Arabic text.
def ar():
    # Open and read in the file.
	f_in = open("../data/ted/ar-en-ted.tmx", 'rU')
	lines = f_in.readlines()
	f_in.close()

	# RegEx that will match Arabic lines.
	rx_ar = re.compile('<tuv xml:lang="ar">')

    # RegEx that will match the line with the number of the talk.
	rx_ar2 = re.compile('<tuv xml:lang="ar"><seg>\d+</seg></tuv>')

    # RegEx that will match the line with the link to the talk.
	rx_http_ar = re.compile('<tuv xml:lang="ar"><seg>http://www.ted.com/talks/')

    # Create new variable: ar.
	ar = []

    # Create counter_ar, set to zero.
	counter_ar = 0

    # Create variable num to store the file name.
	num = None

    # Create for loop over "lines".
	for line in lines:
         # Strip of whitespace.
		line = line.strip()

        # If http-RegEx matches the line
        # and counter_ar is > 0:
        # delete metadata from ar,
        # save ar to file;
        # reset ar.
		if rx_http_ar.match(line):
			if counter_ar > 0:
				del ar[0:4]
				f_out_ar = open("../out/ted/ar/" + str(num) + "ar.txt", 'w')
				str_ar = '\n'.join(ar)
				str_ar = re.sub(r"\n", " ", str_ar)
				f_out_ar.write(str_ar)
				ar = []
        # Else:
        # If the RegEx matches the number of the talk
        # and len(ar) is less than 5:
        # delete XML tags and save the number in variable: num.
        # If RegEx matches a regular line:
        # Delete XML, append line to ar.
		else:
			if rx_ar2.match(line):
				if len(ar) < 5:
					num = re.sub(r"</?[^>]*>","", line)
					#print("num", num)
					counter_ar += 1
			if rx_ar.match(line):
				line = re.sub(r"</seg></tuv>", "", str(line))
				line = re.sub(r"<tuv xml:lang=\"ar\"><seg>", "", line)
				ar.append(line)


    # If there is data left in ar:
    # get the number of the talk from ar: num,
    # delete metadata; save en to file.
	if ar:
		num = ar[2]
		del ar[0:4]
		f_out_ar = open("../out/ted/ar/" + str(num) + "ar.txt", 'w')
		str_ar = '\n'.join(ar)
		str_ar = re.sub(r"\n", " ", str_ar)
		f_out_ar.write(str_ar)


if language == "en":
	en()
elif language == "ar":
	ar()
