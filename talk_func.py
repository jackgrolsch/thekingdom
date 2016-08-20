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
	num_to_add = spacecount//(random.randint(5,spacecount)+1)
	print num_to_add


	for i in range(0, num_to_add):
		splitted = text.split()
		w_append = random.randint(0,spacecount)
		
		if w_append in p_appended:
			w_append = random.randint(0,spacecount)
		else:
			p_appended.append(w_append)
		
		chartoadd = random.choice(to_append)
		splitted[w_append] = splitted[w_append]+chartoadd
		text = " ".join(splitted)

	#Finish with a closing symbol
	text = text + (random.choice(to_end))

	return text
		
