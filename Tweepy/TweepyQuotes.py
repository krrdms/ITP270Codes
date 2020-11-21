import tweepy
import random
from time import sleep

auth = tweepy.OAuthHandler('xxxx', 'xxxx')
auth.set_access_token('xxxx-xxxx', 'xxxx')
api = tweepy.API(auth)

f=open('verne.txt')
quotes=f.readlines()
f.close()
count=len(quotes)

while count > 0:
    quote = random.choice(quotes)
    try:
        print(quote)
        if quote != '\n':
            api.update_status(quote)
        else:
            pass
    except tweepy.TweepError as e:
        print(e.reason)
    quotes.remove(quote)
    sleep(60 * count * 2)
    count -= 1

