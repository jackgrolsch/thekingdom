#!/usr/bin/env python

import praw
user_agent = ("Francestats a01")

r = praw.Reddit(user_agent = user_agent)
subreddit = r.get_subreddit("france")

for submission in subreddit.get_hot(limit = 5):
	print "Title: ", submission.title
	print "Text: ", submission.selftext
	print "Score: ", submission.score
	print "-----------------------------\n"
