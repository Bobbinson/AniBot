"""""""""""

@Author = Bobbinson

Fetches photos from multiple subreddits and posts to a twitter account in real-time.

"""""""""""

import praw
import tweepy
import time
import os
import sys
import random
import json
import requests
import urllib.request
from urllib.parse import urlparse
from os.path import splitext

from AniBot_config import *


# Add post ID to file
def add_id_to_file(post):
    with open('posted.txt','a') as file:
        file.write(str(post) + "\n")

# Check if post is duplicate/ Have to rework this
'''
def check_for_duplicates(post):
    collect = 0
    with open('posted.txt','r') as file:
        for line in file:
            if post in line:
                collect = 1
    return collect
'''



def post_memes():
    # Connecting to Reddit
    reddit = praw.Reddit('AniBot')
    # Setting up Twitter authentication using secret variables from config file
    auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_token_secret)

    tweep = tweepy.API(auth)
    # Taking out the subreddit names from subreddits.txt
    subreddit_fetch = open('subreddits.txt','r')
    subbreddit_names = subreddit_fetch.read().strip().split("\n")
    subreddit_fetch.close()



    ### Can embed in a while loop for an infinite iteration in a database ###
   # while(True):
    #    time.sleep(1800)

    # Make sure the extension is correct
    check_extension = False

    while check_extension == False:
        post = reddit.subreddit(random.choice(subbreddit_names)).random() # Pick a subreddit at random
        
        ext = post.url[-4:] # Not sure if this is a correct way to retrieve extensions, but it works.
        print(ext)

        for file_type in ['.jpg','.png','.gif']:
            if ( ext == file_type):
                check_extension = True
                break
    
    img_file = "picture" + ext
    urllib.request.urlretrieve(post.url, img_file)
    
    #found = check_for_duplicates(post)
    #if found == 0:
    add_id_to_file(post)
    tweep.update_with_media(img_file)

    os.remove(img_file)
    time.sleep(30)




post_memes()



    





