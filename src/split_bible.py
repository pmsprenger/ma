# split_bible.py
# author : Peter Sprenger
# date : 27.06.2017
# This script splits the English or Arabic Bible in its chapters.

# Import necessary modules.
import sys, re

# Define which language to split via sys.argv
language = sys.argv[1]

# Function that will split the English text.
def en():
	# Open and read in the file.
	f_in = open("../data/bible/eng-x-bible-kingjames.txt")
	lines = f_in.readlines()
	f_in.close()

	# Create RegEx that matches the lines with 8 numbers at the beginning.
	numline = re.compile(r'^[0-9]{4}[0-9][0-9]{3}\s')

	#num_old = 0
	#num_new = 0

	# Set counter to zero.
	counter = 0

	# Create new list "en".
	en = []

	# Create for loop over "lines".
	for line in lines:
		# Strip of whitespace.
		line = line.strip()

		# If the line has 8 numbers at the beginning...
		if numline.match(line):

			# Save number on position 5 in new variable.
			num_new = re.sub(r'^[0-9]{4}([0-9]).*', r'\1', line)

			# Set num_old as num_new if length of en is over 2.
			if len(en) < 2:
				num_old = num_new

			# If num_new is not num_old: add 1 to counter; open a new file with
			# counter as filename; Join the elements in the list with a newline;
			# Substitute the new lines with a whitespace; Write the data to the
			# file and finally empty variable en.
			if num_new != num_old:
				counter += 1
				f_out = open("../out/bible/en/" + str(counter) + "en.txt", 'w')
				str_en = '\n'.join(en)
				str_en = re.sub(r"\n", " ", str_en)
				f_out.write(str_en)
				print("File saved.")
				en = []

			# Delete the numbers in front of the text and save as new variable.
			# Append line to list en.
			line = re.sub(r'^[0-9]{8}\s(.*)', r'\1', line)
			en.append(line)

	# If there is data in variable "en" left, open a last file with counter as
	# file name and repeat process from few lines above.
	if en:
		f_out = open("../out/bible/en/" + str(counter) + "en.txt", 'w')
		str_en = '\n'.join(en)
		str_en = re.sub(r"\n", " ", str_en)
		f_out.write(str_en)
		print("File saved. Process finished.")


# Run this function if language of the files is Arabic.
def ar():
	f_in = open("../data/bible/arb-x-bible.txt")
	lines = f_in.readlines()
	f_in.close()

	numline = re.compile(r'^[0-9]{4}[0-9][0-9]{3}\s')

	counter = 0

	ar = []

	for line in lines:
		line = line.strip() # strip of whitespace

		if numline.match(line):

			num_new = re.sub(r'^[0-9]{4}([0-9]).*', r'\1', line)

			if len(ar) < 2:
				num_old = num_new

			if num_new != num_old:
				counter += 1
				f_out = open("../out/bible/ar/" + str(counter) + "ar.txt", 'w')
				str_ar = '\n'.join(ar)
				str_ar = re.sub(r"\n", " ", str_ar)
				f_out.write(str_ar)
				print("File saved.")
				ar = []

			line = re.sub(r'^[0-9]{8}\s(.*)', r'\1', line)
			ar.append(line)



	if ar:
		f_out = open("../out/bible/ar/" + str(counter) + "ar.txt", 'w')
		str_ar = '\n'.join(ar)
		str_ar = re.sub(r"\n", " ", str_ar)
		f_out.write(str_ar)
		print("File saved. Process finished.")


if language == "en":
	en()
elif language == "ar":
	ar()
