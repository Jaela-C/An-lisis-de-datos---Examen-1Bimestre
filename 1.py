import couchdb
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json

#API
ckey = "B8fR8M4GoiypS3dyjHGXLZt43"
csecret = "6BpiXcpFQuJeTciAU0xpeZ8ej2vZaifbF8Q5i8Mv7CkJjfBofI"
atoken = "1339679861196075008-bbb6dICJ0EqpZdolHVwNGEyvMoJDBZ"
asecret = "rG87TqnxMg5HFFj3GPwWdrtd5kdu5htcKddu573o2hRJB"

class listener(StreamListener):
    
    def on_data(self, data):
        dictTweet = json.loads(data)
        try:
            
            dictTweet["_id"] = str(dictTweet['id'])
            doc = db.save(dictTweet)
            print("SAVED" + str(doc) + "=>" + str(data))
        except:
            print("Already exists")
            pass
        return True
    
    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())

server = couchdb.Server('http://jaela:654321@localhost:5984/')
try:
    db = server.create('mario_kart')
except:
    db = server['mario_kart']
twitterStream.filter(track = ['mario kart'])