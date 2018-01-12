# file: 	   split_un.py
# author:      Peter Sprenger
# date:        29.05.2017
# description: Extract all English and all Arabic lines from the
# 			   UN Corpora and put them in separate txt files,
# 			   sorted by resolutions.

# Import necessary modules.
import sys, re

# Set sys.argv[1] as language - en/ar as options.
language = sys.argv[1]

# Function that will split the English text.
def en():
	# Open and read in the file.
	f_in = open("../data/un/ar-en-un.tmx", 'rU')
	lines = f_in.readlines()
	f_in.close()

	# RegEx that will match English lines.
	rx_en = re.compile("<tuv xml:lang=\"en\"><seg>")

	# Create variable that will store the resolutions: en.
	en = []

	# RegEx that will trigger the lines in variable en to be saved to a file.
	rx_res_1 = re.compile(r'<tuv xml:lang="en"><seg>RESOLUTIONS? \d+/\d+\s?\S?.')

	# RegEx's that will match the no. of a resolution.
	rx_en_num1 = re.compile(r"<tuv xml:lang=\"en\"><seg>\d+/\d+\.?\s?(A|B)?")
	rx_en_num2 = re.compile(r"^\d+/\d+ (A|B)\.")

	# Create variable num to store the file name.
	num = None

	# Create counter_en, set to zero.
	counter_en = 0

	# Create for loop over "lines".
	for line in lines:
		# Strip off whitespace.
		line = line.strip()

		# If RegEx 1 matches and
		# counter_en is > 0,
		# append numline to en first,
		# then save en to file.
		# Reset en.
		if rx_res_1.match(line):
			if counter_en > 0:
				en.append(numline)
				f_out_en = open("../out/un/en/" + str(num) + ".en.txt", 'w')
				str_en = '\n'.join(en)
				str_en = re.sub(r"\n", " ", str_en)
				f_out_en.write(str_en)
				en = []

		else:
			# If RegEx matches the line with the no. of the resolution:
			# delete the XML at the beginning and end of line,
			# save line to variable: numline,
			# save the no. itself to variable: num.
			# Add 1 to counter_en.
			if rx_en_num1.match(line):
				line = re.sub(r"</seg></tuv>", "", str(line))
				line = re.sub(r"<tuv xml:lang=\"en\"><seg>", "", line)
				numline = line
				if rx_en_num2.match(line):
					num = re.sub(r"^(\d+)/(\d+) ([A|B]).*", r"\1-\2-\3", line)
				else:
					num = re.sub(r"(\d+)/(\d+)\..*", r"\1-\2", line)
				counter_en += 1

			# Else if:
			# Delete XML in the beginning and the end of line.
			# Pass if the line starts with certain phrases.
			# Append the line to variable: en.
			elif rx_en.match(line):
				line = re.sub(r"</seg></tuv>", "", str(line))
				line = re.sub(r"<tuv xml:lang=\"en\"><seg>", "", line)
				if line.startswith("In favour:"):
					pass
				elif line.startswith("Abstaining:"):
					pass
				elif line.startswith("Against:"):
					pass
				elif line.startswith("Adopted at the"):
					pass
				elif line.startswith("* In favour"):
					pass
				elif line.startswith("Abstentions:"):
					pass
				else:
					en.append(line)

	# If there is content in variable en left:
	# Append numline to en.
	# Save en to file.
	if en:
		en.append(numline)
		f_out_en = open("../out/un/en/" + str(num) + ".en.txt", 'w')
		str_en = '\n'.join(en)
		str_en = re.sub(r"\n", " ", str_en)
		f_out_en.write(str_en)


# Function that will split the Arabic text.
def ar():
	# Open and read in the file.
	f_in = open("../data/un/ar-en-un.tmx", 'rU')
	lines = f_in.readlines()
	f_in.close()

	# RegEx that will match Arabic lines.
	rx_ar = re.compile("<tuv xml:lang=\"ar\"><seg>")

	# Create new variable: ar.
	ar = []

	# RegEx that will trigger the lines in variable ar to be saved to a file.
	rx_res_1 = re.compile(r'<tuv xml:lang="en"><seg>RESOLUTIONS? \d+/\d+\s?\S?.')


	# Three RegExs that match the lines with the number of the TED talk.
	rx_ar_num = re.compile(r"<tuv xml:lang=\"ar\"><seg>\d+/\d+\.?\s?")
	rx_alif = re.compile(r"<tuv xml\:lang=\"ar\"><seg>\d+/\d+ \u0623\u0644\u0641")
	rx_ba = re.compile(r"<tuv xml\:lang=\"ar\"><seg>\d+/\d+ \u0628\u0627\u0621")

	# Create counter_ar, set to zero.
	counter_ar = 0

	# Create variable num to store the file name.
	num = None

	# Create for loop over "lines".
	for line in lines:
		# Strip of whitespace.
		line = line.strip()

		# If RegEx 1 matches and
		# counter_ar is > 0,
		# append numline to ar first,
		# then save en to file.
		# Reset ar.
		if rx_res_1.match(line):
			if counter_ar > 0:
				ar.append(numline)
				f_out_ar = open("../out/un/ar/" + str(num) + ".ar.txt", 'w')
				str_ar = '\n'.join(ar)
				str_ar = re.sub(r"\n", " ", str_ar)
				f_out_ar.write(str_ar)
				ar = []

		# Else if to match all possible variations
		# of the no of the resolution.
		# For each instance:
		# delete XML tags, save content of num to variable: numline.
		# Save the no. of the resolution to variable: num.
		# Add 1 to counter_ar.
		elif rx_alif.match(line):
			num = re.sub(r"</?[^>]*>","", line)
			numline = num
			num = re.sub(r"(\d+)/(\d+) \u0623\u0644\u0641.*", r"\1-\2-A", num)
			counter_ar += 1

		elif rx_ba.match(line):
			num = re.sub(r"</?[^>]*>","", line)
			numline = num
			num = re.sub(r"(\d+)/(\d+) \u0628\u0627\u0621.*", r"\1-\2-B", num)
			counter_ar += 1

		elif rx_ar_num.match(line):
			num = re.sub(r"</?[^>]*>","", line)
			numline = num
			num = re.sub(r"^(\d+)/(\d+).*", r"\1-\2", num)
			counter_ar += 1

		# Else:
		# Delete XML at the beginning and end of line.
		# Pass if line begins with certain passages in Arabic.
		# Append all other lines to en.
		else:
			if rx_ar.match(line):
				line = re.sub(r"</seg></tuv>", "", str(line))
				line = re.sub(r"<tuv xml:lang=\"ar\"><seg>", "", line)
				if line.startswith(r"\u0627\u0644\u0645\u0624\u064A\u062F\u0648\u0646:"):
					pass
				elif line.startswith(r"\u0627\u0644\u0645\u0639\u0627\u0631\u0636\u0648\u0646:"):
					pass
				elif line.startswith(r"\u0627\u062A\u062E\u0630 \u0641\u064A"): # ~38 instances more in English?
					pass
				elif line.startswith(r"\*\s\-\s\u0627\u0644\u0645\u0624\u064A\u062F\u0648\u0646"):
					pass
				elif line.startswith(r"\u0627\u0644\u0645\u0645\u062A\u0646\u0639\u0648\u0646:"):
					pass
				else:
					ar.append(line)

	# If there is content in variable ar left:
	# Append numline to ar.
	# Save ar to file.
	if ar:
		ar.append(numline)
		f_out_ar = open("../out/un/ar/" + str(num) + ".ar.txt", 'w')
		str_ar = '\n'.join(ar)
		str_ar = re.sub(r"\n", " ", str_ar)
		f_out_ar.write(str_ar)

if language == "en":
	en()
elif language == "ar":
	ar()
