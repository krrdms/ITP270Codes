import tweepy
from time import sleep
from credentials import *

auth = tweepy.OAuthHandler('xxxx', 'xxxx')
auth.set_access_token('xxxx-xxxx', 'xxxx')
api = tweepy.API(auth)

my_file=open('quotes.txt','r')
file_lines=my_file.readlines()
my_file.close()

for line in file_lines:
    try:
        print(line)
        if line != '\n':
            sleep(60)
            api.update_status(line)
        else:
            pass
    except tweepy.TweepError as e:
        print(e.reason)
    sleep(60)