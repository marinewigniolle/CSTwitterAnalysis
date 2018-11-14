from twitter_connection_setup import twitter_setup

def collect():
    connexion = twitter_setup()
    tweets = connexion.search("@EmmanuelMacron",language="french",rpp=100,show_user=True)
    for tweet in tweets:
        print(tweet.text)

collect()


