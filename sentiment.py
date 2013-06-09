import sys
import oauth2 as oauth
import urllib2 as urllib
from urllib2 import urlopen
import json

access_token_key = " " # Enter your Twitter access token
access_token_secret = " " # Enter your Twitter access token secret

consumer_key = " " # Enter your consumer key
consumer_secret = " " # Enter your consumer secret

_debug = 0

oauth_token    = oauth.Token(key=access_token_key, secret=access_token_secret)
oauth_consumer = oauth.Consumer(key=consumer_key, secret=consumer_secret)

signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

http_method = "GET"


http_handler  = urllib.HTTPHandler(debuglevel=_debug)
https_handler = urllib.HTTPSHandler(debuglevel=_debug)

file = open(' ') # Enter the text file with the list of words and ratings here
scores = {}
for line in file:
    term, score = line.split("\t")
    scores[term] = int(score)

print scores.items() # Print every (term, score) pair in the dictionary

def lines(fp):
    print str(len(fp.readlines()))
