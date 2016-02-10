import sys
import fileinput
import re

"""
This is the twtt module. It is responsible for tokenizing and tagging tweets
from the csv files taken from the Sentiment140 Corpus.

The program takes in a tweet file, following the form specified in the
Assignment guidelines and convert it to the normalized form which is also
specified in the guidelines.
"""


""" Remove any HTML tags and attributes. """
def remove_html_tag_and_attr():
	return

""" Replace any HTML character code with ASCII equivalent. """
def replace_html_char_code():
	# use re to find the html code then use unichr() to convert 
	# then use replace() to change it
	return

""" Remove URLs (tokens beginning with www/http). """
def remove_urls():
	return

""" Remove the first char of twitter usernames '@' and hastags '#'. """
def remove_at_and_hash():
	return

""" Remove the first char of twitter usernames '@' and hastags '#'. """
def remove_at_and_hash():
	return

""" Place every sentence within a tweet on its own line. """
def sentence_new_line():
	return

""" Keep Ellipsis and other multiple punctuations together. """
def ellip_and_mult():
	return

# TO-DO: This may not be a function, this may be something we incorporate
# 		 into our other functions
""" Keep Ellipsis and other multiple punctuations together. """
def ellip_and_mult():
	return

""" Make each token, including clitics, separated by whitespace. """
def add_whitespace():
	return

""" Tag each token with its associated PoS. """
def POS_tag():
	return

""" Add the appropriate demarcation before each tweet including tweet class. """
def add_demarcation():
	return

""" Pre-process the tweets """
def pre_process():
	return

if __name__ == "__main__":

	#### what i have so far:
	#### 	- handles arguments and puts them in the correct variables
	#### 	- goes through the file line by line and separates only the tweet part
	####	- separated line are output in the output file

	# Argument Handling
	if len(sys.argv) == 3:
		# has NO group ID
		print 'Number of arguments:', len(sys.argv), 'arguments.'
		input_file = str(sys.argv[1])
		output_file = str(sys.argv[2])
		print 'Input file :', input_file
		print 'Output file :', output_file

		# Open output file
		f = open(output_file,'w')

		# Read Line from File and separates tweet
		for line in fileinput.input([input_file]):

			# This puts each line into an array so we can modify it individually. 
			line_arr = line.split(',',5)
			print line_arr[-1]
			html_pattern = re.compile(r'<.*?>')
			if html_pattern.search(line_arr[-1]):
				# Gets rid of HTML tags.
				no_html = re.sub(html_pattern, "", line_arr[-1])
				no_html = no_html.strip()
				print 'True\n '
				print no_html

			else:
				print 'False\n'

		# Close output file
		f.close()


	elif len(sys.argv) == 4:
		# has group ID
		print 'Number of arguments:', len(sys.argv), 'arguments.'
		input_file = str(sys.argv[1])
		group_id = str(sys.argv[2])
		output_file = str(sys.argv[3])
		print 'Input file :', input_file
		print 'Output file :', output_file
		print 'Group ID :', group_id

	else:
		# Incorrect amount of arguments
		print "Incorrect amount of arguments"


