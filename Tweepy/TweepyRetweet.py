import tweepy
from time import sleep

auth = tweepy.OAuthHandler('xxxx', 'xxxx')
auth.set_access_token('xxxx-xxxx', 'xxxx')
api = tweepy.API(auth)

for tweet in tweepy.Cursor(api.search, q=('#ITP270 OR #ITP270 -filter:retweets'), lang='en').items(6):
    try:
        # Add \n escape character to print() to organize tweets
        print('\nTweet by: @' + tweet.user.screen_name)

        # Retweet tweets as they are found
        tweet.retweet()
        print('Retweeted the tweet')

    except tweepy.TweepError as e:
        print(e.reason)

    except StopIteration:
        break
    sleep(90)