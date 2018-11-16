from textblob import TextBlob

import nltk
nltk.download('punkt')

def analyse_opinion_candidate(data):
    # Fonction renvoyant l'analyse de l'opinion et qui prend en entrée une liste de tweets ne concernant qu'un seul candidat.

    ## Création de la liste des polarités de chaque tweet
    L = []

    ## Récupération des polarités de chaque tweet
    for tweet in data['tweet_textual_content']:
        t=TextBlob(tweet)
        L.append(t.sentiment.polarity)

    ## Création des listes de tweets positifs, neutres et négatifs
    pos_tweets = []
    neu_tweets = []
    neg_tweets = []

    for k in range(len(L)):
        if L[k]>0:
            pos_tweets.append(data['tweet_textual_content'][k])
        if L[k]=0
            neu_tweets.append(data['tweet_textual_content'][k])
        if L[k]<0:
            neg_tweets.append(data['tweet_textual_content'][k])

    print("Percentage of positive tweets: {}%".format(len(pos_tweets)*100/len(data['tweet_textual_content'])))
    print("Percentage of neutral tweets: {}%".format(len(neu_tweets)*100/len(data['tweet_textual_content'])))
    print("Percentage de negative tweets: {}%".format(len(neg_tweets)*100/len(data['tweet_textual_content'])))
