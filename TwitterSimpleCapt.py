# _*_ coding:utf-8 _*_

# TweetSimpleCapt
# @author Robert Carlos                                 #
# email robert.n.roll@gmail.com                         #
# 2016-12-23 (CC BY 3.0 BR)                             #

from datetime import datetime
from pymongo import MongoClient
import secret as SC
import pymongo
import tweepy
import time

CONSUMER_KEY = SC.KEY
CONSUMER_SECRET = SC.SECRET
ACCESS_TOKEN = SC.TOKEN
ACCESS_TOKEN_SECRET = SC.TOKEN_SECRET
AUTH = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
AUTH.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

TRACKER = ['a','b','c','d','e','f','g','h','i','j','k','l',
           'm','n','o','p','q','r','s','t','u','v','w','x','y','z',
           '1','2','3','4','5','6','7','8','9','0',
           '@','#','$','%','&','*']

TW_COUNT = 0
TW_TOTAL = 215088
START = datetime.now()

def mongo_insert(screen_name,text,st_created_at,
                 followers,following,statuses_count,
                 lang,us_created_at,place,country):
    client = MongoClient()
    db = client.Twitter
    db.tweets.insert_one(
        {
            'screen_name'   :   screen_name,  
            'text'          :   text,
            'st_created_at' :   st_created_at,   
            'followers'     :   followers,
            'following'     :   following,
            'statuses_count':   statuses_count,
            'lang'          :   lang,
            'us_created_at' :   us_created_at,
            'place'         :   place,
            'country'       :   country,
        }
    )
    client.close()

def mongo_index():
    print 'Indexando'
    client = MongoClient()
    db = client.Twitter
    result = db.tweets.create_index(
        [
            (
                "text", pymongo.ASCENDING
            )
        ]
    )
    print 'Index',result,'criado'
    client.close()

class CustomStreamListener(tweepy.StreamListener):
    def on_status(self,status):
        global TW_COUNT
        global TW_TOTAL
        global END
        
        if TW_COUNT < TW_TOTAL:
            try:
                END = datetime.now()
                TW_COUNT += 1
                print 'Tweets coletados', TW_COUNT
                screen_name = status.user.screen_name
                text = status.text
                st_created_at = status.created_at
                followers = status.user.followers_count
                following = status.user.friends_count
                statuses_count = status.user.statuses_count
                lang = status.user.lang
                us_created_at = status.user.created_at
                if status.place is not None:
                    place = status.place.full_name
                    country = status.place.country
                else:
                    place = None
                    country = None
                mongo_insert(screen_name,text,st_created_at,
                             followers,following,statuses_count,
                             lang,us_created_at,place,country)
            except BaseException, e:
                print 'Falha ao inserir', str(e)
                time.sleep(5)
                pass
        else:
            mongo_index()
            print 'Concluido!\n',END - START
            return False

    def on_error(self, status_code):
        print 'Houve um erro: ', status_code
        if status_code == 420:
            time.sleep(900)
            return True
        return True

    def on_timeout(self):
        print 'Aguarde...'
        time.sleep(5)
        return True

if __name__ == '__main__':
    tapi = tweepy.streaming.Stream(AUTH, CustomStreamListener())
    tapi.filter(track = TRACKER)
