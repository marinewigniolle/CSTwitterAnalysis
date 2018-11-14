from CSTwitterAnalysis.Twitter_collect.Twitter_connection_setup import  twitter_setup
def collect():
    connexion = twitter_setup()
    tweets = connexion.search("#Emmanuel",language="french",rpp=100)
    for tweet in tweets:
        print(tweet.text)
collect()

def collect_by_user(user_id):
    connexion = twitter_setup()
    statuses = connexion.user_timeline(id = user_id, count = 200)
    for status in statuses:
        print(status.text)
    return statuses
## ce code renvoie les 200 derniers statuts de l'utilisateur choisi
collect_by_user(1144707571)
