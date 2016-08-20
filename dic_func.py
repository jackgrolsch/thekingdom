#!/usr/bin/env python
# coding: utf8

import pdb
import re
import os
import string
import random

#Here be the functions used for the bots to find word to use.

#___ su_pick ____

#Simple Unique pick. Pick a single word base on the argument passed and not passed
#Arguments: dictionnary path, intent, tone

def su_pick(dic_path, intent, tone):

	#Load dictionnary: for optimisation purposes, maybe do that in the bot code and pass it to the method
	with open(dic_path) as dictionnary:
		lines = dictionnary.read().splitlines() #list of lines

	#Depending on the arguments given by the bot, use a picking method
	
	final_list = [] #This will be our narrowed word choices
	
	#Intent only
	if 'intent' in locals() and not 'tone' in locals():
		for line in lines:
			if ' '+intent+' ' in line:
				final_list.append(line)	

	#Tone only
	if 'intent' not in locals() and 'tone' in locals():
		for line in lines:
			if ' '+tone+' ' in line:
				final_list.append(line)
	#Intent and tone
	if 'intent' in locals() and 'tone' in locals():
		pick_by_intent = []
		for line in lines:
			if ' '+intent+' ' in line:
				pick_by_intent.append(line)

		for line in pick_by_intent:
			if ' '+tone+' ' in line:
				final_list.append(line)
		
	#regardless of wether a single line was taken form the dictionnary or multiple ones, we will
	#randomly pick one word from the list.
	
	if not final_list:
		return
	else:
		chosen_line = random.choice(final_list)
		splited_line = chosen_line.split()
		chosen_word = splited_line[0]
		return chosen_word

