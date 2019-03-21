#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
#import argparse
import sys
import os

#print the name of this file
print('code name is: ',sys.argv[0])

# if input argument is given, the first argument must be a path 
# to a file where the downloaded tweets are saved 
if len(sys.argv) > 1:
    filename=sys.argv[1]
else:
    filename='tweets.json'

print('saving data to file: ',filename)
fhandle=open(filename,'w')

# if input argument is given, the second, third, .. 
# are tweet topics to use as a filter. The tweets downloaded
# will have one of the topics in their text or hashtag 
if len(sys.argv) > 2:
    TweetKeyword=[sys.argv[i+2] for i in range(len(sys.argv)-2)]
else:
    TweetKeyword=['Africa','big data']

#print the tweet topics 
print('TweetKeywords are: ',TweetKeyword)
print('For testing case, please interupt the downloading process using ctrl+x after about 5 mins ')

#Variables that contains the user credentials to access Twitter API 
consumer_key = os.environ.get('TWITTER_API_KEY')
consumer_secret = os.environ.get('TWITTER_API_SECRET')
access_token = os.environ.get('TWITTER_ACCESS_TOKEN')
access_token_secret = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        #print data
        fhandle.write(data)
        return True

    def on_error(self, status):
        print (status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    
    stream = Stream(auth, l)
    
    #This line filter Twitter Streams to capture data by the keywords: first argument to this code
    stream.filter(track=TweetKeyword)
