#!/usr/bin/env python
# coding: utf8

import pdb
import re
import os
import string
import random

#Here be the functions used by the bots to put their text in shape.

#____ s_punctuate ____

#Add punctuation to a text, and some reddit formatting. Mostly random.

def s_punctuate(text):
	
	#Method variables
	p_appended = []	
	to_append = [',','.','!','?']
	to_end = ['.','!','?']

	#Capitalize the first letter of the text
	text = text.capitalize()
	
	
	#Add random punctuation
	spacecount = text.count(' ')
	med_length = spacecount//5
	num_to_add = random.randint(1,med_length)


	for i in range(0, num_to_add):
		splitted = text.split()
		w_append = random.randint(0,(len(splitted)-1))
		
		if w_append in p_appended:
			w_append = random.randint(0,(len(splitted)-1))
		else:
			p_appended.append(w_append)
		
		chartoadd = random.choice(to_append)
		splitted[w_append] = splitted[w_append]+chartoadd
		text = " ".join(splitted)

	#Capitalize inside the text, with a badass RE taken from stackoverflow
	def uppercase(matchobj):
		return matchobj.group(0).upper()
	text = re.sub('^([a-z])|[\.|\?|\!]\s*([a-z])|\s+([a-z])(?=\.)', uppercase, text)

	#Finish with a closing symbol
	text = text + (random.choice(to_end))

	return text
		
