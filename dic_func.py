#!/usr/bin/env python
# coding: utf8

import pdb
import re
import os
import string
import random
import dataset

#Here be the functions used for the bots to find word to use.

#___ su_pick ____

#Simple Unique pick. Pick a single word base on the argument passed and not passed
#Arguments: dictionary path, intent, tone

def su_pick(dictionary, intent, tone):

	#Instead of parsing a dictionary, we now query a database. (absolute path for portability)
	#Requires module "dataset" (pip install dataset)
	db = dataset.connect('sqlite:///database/thekingdom.db') #Connect
	table = db[dictionary] #Select the correct table
	words = [] #The list of words we will pick from

	#Depending on the arguments given by the bot, use a picking method
	#Intent only
	if 'intent' in locals() and not 'tone' in locals():
		rows = table.find(intent=intent)
		for row in rows:
			words.append(row['word'])
	#Tone only
	if 'intent' not in locals() and 'tone' in locals():
		rows = table.find(tone=tone)
		for row in rows:
			words.append(row['word'])
	#Intent and tone
	if 'intent' in locals() and 'tone' in locals():
		rows = table.find(intent=intent,tone=tone)
		for row in rows:
			words.append(row['word'])
	if not words:
		return
	else:
		chosen_word = random.choice(words)
		return chosen_word

#___ sf_gen_intent ___

#Instead of creating a random sentence, this method try to construct something cohesive around
#a given theme

def sf_gen_intent(dictionary, theme):

	#DB connection and table selection
	db = dataset.connect('sqlite:///database/thekingdom.db')
	table = db[dictionary]
	output = []
	
	#Theme: giving an opinion on something (share_op)
	if theme == 'share_op':

		words = []		

		rows = table.find(intent='call')
		for row in rows:
			words.append(row['word'])
		subject = random.choice(words)

		output.append(subject)
		print output
		
		#Is the bot appreciating the subject?
		tone = random.choice(['neutral','friendly','unfriendly'])

		#how many adjectives?
		adj_n = random.randrange(1,5)

		#pick them according to his opinion
		for i in range(0,adj_n):
			su_pick(dictionnary, 'qualify', tone)

		#add random
		 

sf_gen_intent('pelb', 'share_op')
