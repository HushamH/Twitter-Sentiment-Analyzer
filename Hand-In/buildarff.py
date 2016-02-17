import sys
import fileinput
import re

def first_person_pronouns(line, counter_list):

	i = re.compile(r"[\s\b\n][Ii]+/")
	me = re.compile(r"[\s\b\n][Mm]+[Ee]+/")
	my = re.compile(r"[\s\b\n][Mm]+[Yy]+/")
	mine = re.compile(r"[\s\b\n][Mm]+[Ii]+[Nn]+[Ee]+/")
	we = re.compile(r"[\s\b\n][Ww]+[Ee]+/")
	us = re.compile(r"[\s\b\n][Uu]+[Ss]+/")
	our = re.compile(r"[\s\b\n][Oo]+[Uu]+[Rr]+/")
	ours = re.compile(r"[\s\b\n][Oo]+[Uu]+[Rr]+[Ss]+/")

	i_count = len(re.findall(i, line))
	me_count = len(re.findall(me,line))
	my_count = len(re.findall(my,line))
	mine_count = len(re.findall(mine,line))
	we_count = len(re.findall(we,line))
	us_count = len(re.findall(us,line))
	our_count = len(re.findall(our,line))
	ours_count = len(re.findall(ours,line))

	counter_list[0] = i_count + me_count + my_count + mine_count + we_count + us_count + our_count + ours_count

	return counter_list

def second_person_pronouns(line, counter_list):

	you = re.compile(r"[\s\b\n][Yy]+[Oo]+[Uu]+/")
	your = re.compile(r"[\s\b\n][Yy]+[Oo]+[Uu]+[Rr]+/")
	yours = re.compile(r"[\s\b\n][Yy]+[Oo]+[Uu]+[Rr]+[Ss]+/")
	u = re.compile(r"[\s\b\n][Uu]+/")
	ur = re.compile(r"[\s\b\n][Uu]+[Rr]+/")
	urs = re.compile(r"[\s\b\n][Uu]+[Rr]+[Ss]+/")

	you_count = len(re.findall(you, line))
	your_count = len(re.findall(your,line))
	yours_count = len(re.findall(yours,line))
	u_count = len(re.findall(u,line))
	ur_count = len(re.findall(ur,line))
	urs_count = len(re.findall(urs,line))

	counter_list[1] = (you_count + your_count + yours_count + u_count + ur_count + urs_count)

	return counter_list

def third_person_pronouns(line, counter_list):

	he = re.compile(r"[\s\b\n][Hh]+[Ee]+/")
	him = re.compile(r"[\s\b\n][Hh]+[Ii]+[Mm]+/")
	his = re.compile(r"[\s\b\n][Hh]+[Ii]+[Ss]+/")
	she = re.compile(r"[\s\b\n][Ss]+[Hh]+[Ee]+/")
	her = re.compile(r"[\s\b\n][Hh]+[Ee]+[Rr]+/")
	hers = re.compile(r"[\s\b\n][Hh]+[Ee]+[Rr]+[Ss]+/")
	it = re.compile(r"[\s\b\n][Ii]+[Tt]+/")
	its = re.compile(r"[\s\b\n][Ii]+[Tt]+[Ss]+/")
	they = re.compile(r"[\s\b\n][Tt]+[Hh]+[Ee]+[Yy]+/")
	them = re.compile(r"[\s\b\n][Tt]+[Hh]+[Ee]+[Mm]+/")
	their = re.compile(r"[\s\b\n][Tt]+[Hh]+[Ee]+[Ii]+[Rr]+/")
	theirs = re.compile(r"[\s\b\n][Tt]+[Hh]+[Ee]+[Ii]+[Rr]+[Ss]+/")

	he_count = len(re.findall(he, line))
	him_count = len(re.findall(him,line))
	his_count = len(re.findall(his,line))
	she_count = len(re.findall(she,line))
	her_count = len(re.findall(her,line))
	hers_count = len(re.findall(hers,line))
	it_count = len(re.findall(it,line))
	its_count = len(re.findall(its,line))
	they_count = len(re.findall(they,line))
	them_count = len(re.findall(them,line))
	their_count = len(re.findall(their,line))
	theirs_count = len(re.findall(theirs,line))

	counter_list[2] = he_count + him_count + his_count + she_count + her_count + hers_count + it_count + its_count + they_count + them_count + their_count + theirs_count

	return counter_list

def coordinating_conjunctions(line, counter_list):
	
	num_for = len(re.findall(r"[\s\b\n][Ff]+[Oo]+[Rr]+/", line))
	num_and = len(re.findall(r"[\s\b\n][Aa]+[Nn]+[Dd]+/", line))
	num_nor = len(re.findall(r"[\s\b\n][Nn]+[Oo]+[Rr]+/", line))
	num_but = len(re.findall(r"[\s\b\n][Bb]+[Uu]+[Tt]+/", line))
	num_or = len(re.findall(r"[\s\b\n][Oo]+[Rr]+/", line))
	num_yet = len(re.findall(r"[\s\b\n][Yy]+[Ee]+[Tt]+/", line))
	num_so = len(re.findall(r"[\s\b\n][Ss]+[Oo]+/", line))
	num_amp = len(re.findall(r"[\s\b\n]&+/", line))

	counter_list[3] = (num_for + num_and + num_nor + num_but + num_or + num_yet + num_so + num_amp)

	return counter_list 

def past_tense_verbs(line, counter_list):

	num_vbd = len(re.findall(r"\w+/VBD\s", line))
	num_vbn = len(re.findall(r"\w+/VBN\s", line))
	counter_list[4] = num_vbd + num_vbn
	
	return counter_list

def future_tense_verbs(line, counter_list):

	num_ll = len(re.findall(r"\s'/[A-Z#$.,:()\"\']+\sll", line))
	num_will = len(re.findall(r"[\s\b\n][Ww]+[Ii]+[Ll]+[Ll]+/MD", line))
	num_gonna = len(re.findall(r"[\s\b\n][Gg]+[Oo]+[Nn]+[Nn]+[Aa]+", line))
	num_going_to = len(re.findall(r"[\s\b\n][Gg]+[Oo]+[Ii]+[Nn]+[Gg]+/[A-Z$]+\s[Tt]+[Oo]/[A-Z$]+\s\w+/VB", line))

	counter_list[5] = num_ll + num_will + num_gonna + num_going_to

	return counter_list

def commas(line, counter_list):
	regex = re.compile(r",/")
	
	found = re.search(regex, line)
	if found:
		counter_list[6] = len(re.findall(regex, line))

	return counter_list

def colons_semi_colons(line, counter_list):

	regex = re.compile(r"[:;]/")
	
	found = re.search(regex, line)
	if found:
		counter_list[7] = len(re.findall(regex, line))

	return counter_list

def dashes(line, counter_list):
	
	regex = re.compile(r"-")
	
	found = re.search(regex, line)
	if found:
		counter_list[8] = len(re.findall(regex, line))

	return counter_list

def parentheses(line, counter_list):
	regex = re.compile(r"\(/|\)/")
	
	found = re.search(regex, line)
	if found:
		counter_list[9] = len(re.findall(regex, line))

	return counter_list

def ellipses(line, counter_list):

	num_ellipses = len(re.findall(r"\s..+/:",line))

	counter_list[10] = num_ellipses	
	return counter_list

def common_nouns(line, counter_list):

	num_cn= len(re.findall(r"\w+/NNS*\s", line))
	counter_list[11] = num_cn
	
	return counter_list

def proper_nouns(line, counter_list):
	
	num_pn= len(re.findall(r"\w+/NNPS*\s", line))
	counter_list[12] = num_pn

	return counter_list

def adverbs(line, counter_list):
	
	num_adv= len(re.findall(r"\w+/RB[RS]*\s", line))
	counter_list[13] = num_adv

	return counter_list

def wh_words(line, counter_list):
	
	num_wp = len(re.findall(r"\w+/WP\$*\s", line))
	num_wdt = len(re.findall(r"\w+/WDT\s", line))
	num_wrb = len(re.findall(r"\w+/WRB\s", line))
	counter_list[14] = (num_wp + num_wdt + num_wrb)

	return counter_list

def modern_slang(line, counter_list):
	regex = re.compile(r"smh/[A-Z]*|fwb/[A-Z]*|lmfao/[A-Z]*|lmao/[A-Z]*|lms/[A-Z]*\
		|tbh/[A-Z]*|rofl/[A-Z]*|wtf/[A-Z]*|bff/[A-Z]*|wyd/[A-Z]*|lylc/[A-Z]*|brb/[A-Z]*\
		|atm/[A-Z]*|imao/[A-Z]*|sml/[A-Z]*|btw/[A-Z]*|bw/[A-Z]*|imho/[A-Z]*|fyi/[A-Z]*\
		|ppl/[A-Z]*|sob/[A-Z]*|ttyl/[A-Z]*|imo/[A-Z]*|ltr/[A-Z]*|tnx/[A-Z]*|kk/[A-Z]*\
		|omg/[A-Z]*|ttys/[A-Z]*|afn/[A-Z]*|bbs/[A-Z]*|cya/[A-Z]*|ez/[A-Z]*|f2f/[A-Z]*|gtr\
		|ic/[A-Z]*|jk/[A-Z]*|k/[A-Z]*|ly/[A-Z]*|ya/[A-Z]*|nm/[A-Z]*|np/[A-Z]*|plz/[A-Z]*\
		|ru/[A-Z]*|so/[A-Z]*|tc/[A-Z]*|tmi/[A-Z]*|ym/[A-Z]*|ur/[A-Z]*|u/[A-Z]*|sol/[A-Z]*", re.IGNORECASE)
	
	num_slang = (len(re.findall(regex, line)))
	counter_list[15] += num_slang

	return counter_list

def upper_case(line, counter_list):
	regex = re.compile(r"[\s\b\n][A-Z]/[A-Z]*")
	
	num_upper = len(re.findall(regex, line))
	counter_list[16] = num_upper

	return counter_list

def average_token_per_sentence(line, counter_list):
	#### TOKEN = words? IF TOKE CONSISTS OF PUNTUATIONS JUST DO SPACE + 1
	regex = re.compile(r"[\s\b\n][\w&]+/[A-Z]*")

	num_tokens = len(re.findall(regex, line))

	# -2 makes up for the preceding and succeeding \n char. 
	num_sentences = len(re.split("\n",line)) - 2

	counter_list[19] = num_sentences
	counter_list[17] = num_tokens / num_sentences

	return counter_list
	
def average_length_of_tokens(line, counter_list):

	regex = re.compile(r"[\s\b\n]([\w&]+)/[A-Z]*")
	tokens = re.findall(regex, line)
	num_char = 0
	num_tokens = len(tokens)

	for token in tokens:
		num_char += len(token)

	if num_tokens == 0:
		counter_list[18] = 0

	else:
		counter_list[18] = num_char / num_tokens

	return counter_list

def counter(line, counter_list):

	first_person_pronouns(line, counter_list)
	second_person_pronouns(line, counter_list)
	third_person_pronouns(line, counter_list)
	coordinating_conjunctions(line, counter_list)
	past_tense_verbs(line, counter_list)
	future_tense_verbs(line, counter_list)
	commas(line, counter_list)
	colons_semi_colons(line, counter_list)
	dashes(line, counter_list)
	parentheses(line, counter_list)
	ellipses(line, counter_list)
	common_nouns(line, counter_list)
	proper_nouns(line, counter_list)
	adverbs(line, counter_list)
	wh_words(line, counter_list)
	modern_slang(line, counter_list)
	upper_case(line, counter_list)
	average_token_per_sentence(line, counter_list)
	average_length_of_tokens(line, counter_list)

if __name__ == "__main__":

	#### Should we process the input file and output file for a specific extension? ####

	# Argument Handling
	if len(sys.argv) == 3:

		input_file = str(sys.argv[1])
		output_file = str(sys.argv[2])

		# Open output file
		f = open(output_file,'w')

		f.write("@relation tweet\n\n@attribute num_first_person_pronouns numeric\n@attribute num_second_person_pronouns numeric\n@attribute num_third_person_pronouns numeric\n@attribute num_coordinating_conjunction numeric\n@attribute num_past_tense_verbs numeric\n@attribute num_future_tense_verbs numeric\n@attribute num_commas numeric\n@attribute num_colons_semi_colons numeric\n@attribute num_dashes numeric\n@attribute num_parentheses numeric\n@attribute num_ellipses numeric\n@attribute num_common_nouns numeric\n@attribute num_proper_nouns numeric\n@attribute num_adverbs numeric\n@attribute num_wh_words numeric\n@attribute num_modern_slang numeric\n@attribute num_all_caps numeric\n@attribute avg_sentence_length numeric\n@attribute avg_length_token numeric\n@attribute num_sentences numeric\n@attribute tweet_class {0,4}\n\n@data\n")

		tweets = ""

		for line in fileinput.input([input_file]):
			tweets += line

		tweet_arr = re.split(r"<A=\"", tweets)

		for tweet in tweet_arr:
			
			if len(tweet) > 0:
				counter_list = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,int(tweet[0])]
				counter(tweet, counter_list)
				f.write(str(counter_list).strip('[]') + '\n')

		f.close()

	elif len(sys.argv) == 4:

		# has max num tweets
		input_file = str(sys.argv[1])
		output_file = str(sys.argv[2])
		max_twt = int(str(sys.argv[3]))
		

		# Open output file
		f = open(output_file,'w')

		f.write("@relation tweet\n\n@attribute num_first_person_pronouns numeric\n@attribute num_second_person_pronouns numeric\n@attribute num_third_person_pronouns numeric\n@attribute num_coordinating_conjunction numeric\n@attribute num_past_tense_verbs numeric\n@attribute num_future_tense_verbs numeric\n@attribute num_commas numeric\n@attribute num_colons_semi_colons numeric\n@attribute num_dashes numeric\n@attribute num_parentheses numeric\n@attribute num_ellipses numeric\n@attribute num_common_nouns numeric\n@attribute num_proper_nouns numeric\n@attribute num_adverbs numeric\n@attribute num_wh_words numeric\n@attribute num_modern_slang numeric\n@attribute num_all_caps numeric\n@attribute avg_sentence_length numeric\n@attribute avg_length_token numeric\n@attribute num_sentences numeric\n@attribute tweet_class {0,4}\n\n@data\n")

		tweets = ""
		class_tracker = {0: 0, 4: 0}

		for line in fileinput.input([input_file]):
			tweets += line

		tweet_arr = re.split(r"<A=\"", tweets)

		for tweet in tweet_arr:
			
			if len(tweet) > 0:

				cl = int(tweet[0])

				if class_tracker[cl] < max_twt: 
                                        
					counter_list = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,cl]
					counter(tweet, counter_list)
					f.write((str(counter_list).strip('[]') + '\n'))
					class_tracker[cl] += 1
		
		f.close()

	else:
		# Incorrect amount of arguments
		print 'Usage: buildarff.py <input_file> <output_file> <max_num>'


