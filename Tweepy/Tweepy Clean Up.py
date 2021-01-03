import tweepy
import time
import datetime

too_old = 180
too_new = 7
whitelist_tweeters = ["screen_name"]
other_tweeters = []


def get_auth_api(p1, p2, p3, p4):
    auth = tweepy.OAuthHandler(p1, p2)
    auth.set_access_token(p3, p4)
    return tweepy.API(auth, wait_on_rate_limit=True)


def get_favorites(_api_):
    return tweepy.Cursor(_api_.favorites).items()


def get_tweets(_api_):
    return tweepy.Cursor(_api_.user_timeline).items()


def delete_like(tweet, _api_):
    _api_.destroy_favorite(tweet.id)
    time.sleep(6)
    return 1


def delete_retweet(tweet, _api_):
    _api_.destroy_status(tweet)
    time.sleep(6)
    return 1


def delete_favorites(favorites, _api_):
    delete_count = 0
    ignore_count = 0

    for tweet in favorites:
        is_too_old = False
        is_too_new = False
        hard_delete = False

        tweeter = tweet.user.screen_name
        tweet_date = datetime.datetime.strptime(str(tweet.created_at), '%Y-%m-%d %H:%M:%S')
        now = datetime.datetime.utcnow()
        date_delta = (now - tweet_date).days

        if date_delta >= too_old:
            is_too_old = True

        if date_delta <= too_new:
            is_too_new = True

        if tweeter in other_tweeters:
            delete_count += delete_like(tweet, _api_)

        else:

            if tweeter in whitelist_tweeters or is_too_new or is_too_old:
                ignore_count += 1
                time.sleep(0.5)

            else:
                delete_count += delete_like(tweet, _api_)

    return delete_count,ignore_count


def delete_retweets(_api_):
    tweetcount=0
    norts=0
    rts=0
    ignore_count=0
    delete_count=0

    tweets = get_tweets(_api_)
    for tweet in tweets:
        tweetcount += 1
        if int(tweet.retweet_count) == 0:
            norts += 1
            continue
        if int(tweet.retweet_count) > 0:
            try:
                tweeter = tweet.retweeted_status.user.screen_name
            except AttributeError:
                tweeter = "empty"
            rts += 1

        tweet_date = datetime.datetime.strptime(str(tweet.created_at), '%Y-%m-%d %H:%M:%S')
        now = datetime.datetime.utcnow()
        date_delta = (now - tweet_date).days

        if tweeter in other_tweeters:
            delete_count += delete_retweet(tweet.id, _api_)

        else:

            if tweeter in whitelist_tweeters:
                ignore_count += 1
                time.sleep(0.5)

            else:
                if date_delta >= too_old:
                    ignore_count += 1
                    continue
                elif date_delta <= too_new:
                    ignore_count += 1
                    continue
                else:
                    delete_count += (delete_retweet(tweet.id, _api_))

    print("| Count %d: rts %d | no rts %d" % (tweetcount, rts, norts))
    return delete_count,ignore_count


api = get_auth_api('x', 'x',
                   'x', 'x')

status = api.rate_limit_status()
print("/---------------------->")
print("|favorites: %s" % status['resources']['favorites'])
print("|")
print("|")
print("|")
print("|clean up retweets/shares...")
print("|---------------------->")
rt_delete_count, rt_ignore_count = delete_retweets(api)
print("|clean up favorites/likes")
likes = get_favorites(api)
fvr_delete_count, fvr_ignore_count = delete_favorites(likes, api)
print("|---------------------->")
print("| removed %d retweets" % rt_delete_count)
print("| ignored %d retweets" % rt_ignore_count)
print("| removed %d liked-tweets" % fvr_delete_count)
print("| ignored %d liked-tweets" % fvr_ignore_count)
