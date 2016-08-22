#!/usr/bin/env python
# coding: utf8

import praw
import pdb
import re
import os
import string
import random
import dic_func
import talk_func

from pelb1_c import *

#So, I'm initializing a few test variables here, those need to be better integrated later

w_count = random.randint(1, 20); #Later, should use a normal distribution so that the bots post mostly short texts.
intent_list = ['disagree','agree','help','threaten','call','qualify']
tone_list = ['neutral','unfriendly','friendly']

def random_talk(w_count): #The baseline method, just random arguments for random words
	
	content = ''

	for i in range(0,w_count):
		intent = random.choice(intent_list)
		tone = random.choice(tone_list)
		word = dic_func.su_pick('pelb', intent, tone)
		if word:
			content = content+word+' '
	
	content = talk_func.s_punctuate(content)	
	return content

def basic_statement(w_count): #Will try to make more or less coherent sentences
	
	#Basic sentence generator call sf_gen	

def make_new_submission(title_wc, body_wc): #Create a new post
	
	title = random_talk(title_wc)
	body = random_talk(body_wc)
	
	#Send it to reddit
	'''user_agent = ("pelb1")
	r = praw.Reddit(user_agent = user_agent)
	r.login(REDDIT_USERNAME, REDDIT_PASS)
	
	r.submit('KOZfKxpWw9', title, body)'''
	print title+'\n\n'+body 

make_new_submission(20, 100)
