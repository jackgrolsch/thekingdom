#!/usr/bin/env python

import praw
import pdb
import re
import os
import string
import random

from masterscribe_c import *


#Here be the random string generator
def str_generator(size=15, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

#Check the config file
if not os.path.isfile("masterscribe_c.py"):
	print "Config file not found :("
	exit(1)

#Create the reddit instance
user_agent = ("Kingdom a01")
r = praw.Reddit(user_agent = user_agent)
r.login(REDDIT_USERNAME, REDDIT_PASS)

title = str_generator()
text = str_generator(100, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits)
r.submit('KOZfKxpWw9', title, text)
