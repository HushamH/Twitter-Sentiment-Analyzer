import sys
import fileinput
import re
import HTMLParser
import NLPlib

"""
This is the twtt module. It is responsible for tokenizing and tagging tweets
from the csv files taken from the Sentiment140 Corpus.

The program takes in a tweet file, following the form specified in the
Assignment guidelines and convert it to the normalized form which is also
specified in the guidelines.
"""

""" Removes the quotes that wrap the tweet portion of the CSV data """ 
def remove_quotes(line_arr):
	line_arr[-1] = line_arr[-1].replace("\"", "")
	return line_arr

""" Remove any HTML tags and attributes. """
def remove_html_tag_and_attr(line_arr):

	html_pattern = re.compile(r'<.*?>')
	if html_pattern.search(line_arr[-1]):
		# Gets rid of HTML tags.
		no_html = re.sub(html_pattern, "", line_arr[-1])
		no_html = no_html.strip()
		line_arr[-1] = no_html

	return line_arr

""" Replace any HTML character code with ASCII equivalent. """
def replace_html_char_code(line_arr):
	# use re to find the html code then use unichr() to convert 
	# then use replace() to change it
	h = HTMLParser.HTMLParser()
	line_arr[-1] = h.unescape(line_arr[-1])
	
	return line_arr

""" Remove URLs (tokens beginning with www/http). """
def remove_urls(line_arr):

	url_pattern = re.compile(r"(www|http)[:/#.\w]+")
	if url_pattern.search(line_arr[-1]):
		# Gets rid of HTML tags.
		no_url = re.sub(url_pattern, "", line_arr[-1])
		no_url = no_url.strip()
		line_arr[-1] = no_url

	return line_arr

""" Remove the first char of twitter usernames '@' and hastags '#'. """
def remove_at_and_hash(line_arr):
	hash_at_pattern = re.compile(r"[@#]")
	if hash_at_pattern.search(line_arr[-1]):
		# Gets rid of @ and #
		no_hash_at = re.sub(hash_at_pattern, "", line_arr[-1])
		no_hash_at = no_hash_at.strip()
		line_arr[-1] = no_hash_at

	return line_arr

""" Place every sentence within a tweet on its own line. """
def sentence_new_line(line_arr):
	# THIS REGEX IS DEPENDENT ON SEP BY WHITESPACE BEING CALLED FIRST
	# Use regex to match word before EOS punctuation and next 2 char. 
	EOS = re.compile(r"(\w+)\s([\.\?!]+)\s([A-Z])")

	if EOS.search(line_arr[-1]):
		line_arr[-1] = re.sub(EOS, r'\1 \2\n\3', line_arr[-1])

	# MAYBE TO-DO: If word before EOS in the hash of common abreviations, ignore
	return line_arr

# TO-DO: This may not be a function, this may be something we incorporate
# 		 into our other functions
""" Keep Ellipsis and other multiple punctuations together. """
def ellip_and_mult(line_arr):
	"""
	ellip = re.compile(r"[!?.]{2,}")
	if ellip.search(line_arr[-1]):
		# multiple punctuation
		print "YESSSSSSSSSSSSSS"
		
		# DON'T DO ANYTHING
	else:
		##### THIS MAY BE SIMILAR WITH QUESTION 5 SO IF SO USE FUNCTION FROM
		##### QUESTION 5 HERE.
		# only one punctuation
		no_punc = re.sub(ellip, "", line_arr[-1])
		no_punc = no_punc.strip()
		line_arr[-1] = no_punc
		#print no_punc

	#print ellip

	return line_arr
	"""

""" Make each token, including clitics, separated by whitespace. """
def sep_by_whitespace(line_arr):
	# This regex says, split the sentence on any group of 1 or more NON-ALPHANUMERIC CHARACTERS. 
	delimit = re.compile(r"([\W]+)")
	line_arr[-1] =  ' '.join(re.findall('[\S]+', ' '.join(re.split(delimit, line_arr[-1]))))
	return line_arr

""" Tag each token with its associated PoS. """
def POS_tag(line_arr):
    
    tagger = NLPlib.NLPlib()
    parse = re.compile(r"[\n ]")
    sort = ''
    final = ''

    if parse.search(line_arr[-1]):
    	sort = re.split(parse, line_arr[-1])
    	tags = tagger.tag(sort)

    for i in range(len(tags)):
    	final = final + ''.join([sort[i], '/', tags[i]])
    	if i != range(len(tags)):
    		final = final + ''.join(' ')
    
    line_arr[-1] = final

    return line_arr

""" Add the appropriate demarcation before each tweet including tweet class. """
def add_demarcation(line_arr):
	demarc = '<A=' + str(line_arr[0]) + '>\n'
	line_arr[-1] = demarc + line_arr[-1]
	return line_arr

""" Pre-process the tweets """
def pre_process(input_file, output_file):
	# Open output file
	f = open(output_file,'w')

	# Read Line from File and separates tweet
	for line in fileinput.input([input_file]):

		# THESE ARE ORDER SENSITIVE
		# This puts each line into an array so we can modify it individually. 
		line_arr = line.split(',',5)


		
		#print line_arr[-1]

	# Close output file
	f.close()

""" Pre-process the tweets given a group ID. """
def pre_process_with_GID(input_file, output_file, group_id):
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

		pre_process(input_file, output_file)
		# Open output file
		f = open(output_file,'w')

		# Read Line from File and separates tweet
		for line in fileinput.input([input_file]):
			line_arr = line.split(',',5)
			remove_quotes(line_arr)
			line_arr = remove_html_tag_and_attr(line_arr)
			line_arr = replace_html_char_code(line_arr)
			line_arr = remove_urls(line_arr)
			line_arr = remove_at_and_hash(line_arr)
			line_arr = sep_by_whitespace(line_arr)
			# this is where Ellipsis function goes but 
			# we don't need a separate function for it
			line_arr = sentence_new_line(line_arr)
			line_arr = POS_tag(line_arr)
			line_arr = add_demarcation(line_arr)

			#print line_arr[-1]
		
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

		pre_process_with_GID(input_file, output_file, group_id)
		
	else:
		# Incorrect amount of arguments
		print "Incorrect amount of arguments"


