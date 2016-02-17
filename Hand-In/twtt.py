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

	html_pattern = re.compile(r"<.*?>")
	if html_pattern.search(line_arr[-1]):
		# Gets rid of HTML tags.
		no_html = re.sub(html_pattern, "", line_arr[-1])
		no_html = no_html.strip()
		line_arr[-1] = no_html

	return line_arr

""" Replace any HTML character code with ASCII equivalent. """
def replace_html_char_code(line_arr):

	h = HTMLParser.HTMLParser()
        line = ""
        for ch in line_arr[-1]:
            if ord(ch) < 129:
                line += chr(ord(ch))    
        print line        
        line_arr[-1] = h.unescape(line)
	
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
	EOS = re.compile(r"(\w+)\s([\.\?!]+/[A-Z#$.,:()\"\']+)\s([A-Z])")

	if EOS.search(line_arr[-1]):
		line_arr[-1] = re.sub(EOS, r'\1 \2\n\3', line_arr[-1])

	return line_arr

""" Make each token, including clitics, separated by whitespace. """
def sep_by_whitespace(line_arr):

	# This regex says, split the sentence on any group of 1 or more NON-ALPHANUMERIC CHARACTERS. 
	delimit = re.compile(r"([\W]+)")
	line_arr[-1] =  ' '.join(re.findall('[\S]+', ' '.join(re.split(delimit, line_arr[-1]))))
	return line_arr

""" Tag each token with its associated PoS. """
def POS_tag(line_arr, tagger):
    
    final = ''

    tokens = line_arr[-1].split()
    tags = tagger.tag(tokens)

    for i in range(len(tags)):
    	final = final + ''.join([tokens[i], '/', tags[i], ' '])
    
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
        tagger = NLPlib.NLPlib() 
	for line in fileinput.input([input_file]):

		line_arr = line.split(',',5)
		remove_quotes(line_arr)
		line_arr = remove_html_tag_and_attr(line_arr)
		line_arr = replace_html_char_code(line_arr)
		line_arr = remove_urls(line_arr)
		line_arr = remove_at_and_hash(line_arr)
		line_arr = sep_by_whitespace(line_arr)
		line_arr = POS_tag(line_arr,tagger)
		line_arr = sentence_new_line(line_arr)
		line_arr = add_demarcation(line_arr)

		f.write(line_arr[-1] + '\n')

	# Close output file
	f.close()

if __name__ == "__main__":		

	if len(sys.argv) == 4:

		input_file = str(sys.argv[1])
		group_id = int(str(sys.argv[2]))
		output_file = str(sys.argv[3])

		if group_id == 40:
			pre_process(input_file, output_file)

		else:
			print 'Incorrect group number. Please use the correct group number'
		
	else:
		print 'Usage: twtt.py <input_file> <group_num> <output_file>'


