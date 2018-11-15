from CSTwitterAnalysis.Twitter_collect.Twitter_connection_setup import  twitter_setup
import tweepy
def collect():
    connexion = twitter_setup()
    tweets = connexion.search("#Emmanuel",language="french",rpp=100)
    for tweet in tweets:
        print(tweet.text)


def collect_by_user(user_id):
    connexion = twitter_setup()
    statuses = connexion.user_timeline(id = user_id, count = 200)
    for status in statuses:
        print(status.text)
    return statuses
## ce code renvoie les 200 derniers statuts de l'utilisateur choisi



collect_by_user(1144707571)


from tweepy.streaming import StreamListener
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        if  str(status) == "420":
            print(status)
            print("You exceed a limited number of attempts to connect to the streaming API")
            return False
        else:
            return True



def collect_by_streaming():

    connexion = twitter_setup()
    listener = StdOutListener()
    stream=tweepy.Stream(auth = connexion.auth, listener=listener)
    stream.filter(track=['Marine'])

collect_by_streaming()


# test

