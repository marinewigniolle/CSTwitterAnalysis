import panda as pd
import matplotlib.pyplot as plt

def retweets_vs_likes(data):

    tfav = pd.Series(data=data['Likes'].values, index=data['Date'])
    tret = pd.Series(data=data['RTs'].values, index=data['Date'])

    # Likes vs retweets visualization:
    tfav.plot(figsize=(16,4), label="Likes", legend=True)
    tret.plot(figsize=(16,4), label="Retweets", legend=True)

    plt.show()


def nombre_tweets_candidates(data,candidate1,candidate2):
    # Affiche le nombre de tweets contenant le nom du candidate1 et celui du candidaet2

    #création de deux nouvelles colonnes qui indiquent la présence des noms des candidats dans le tweet
    data['Has_candidate1']=(candidate1 in data['tweet_textual_content'])
    data['Has_candidate2']=(candidate2 in data['tweet_textual_content'])


    #création des séries (nombre de likes pour candidat, date) pour candidate1 et candidate2
    tcandidate1 = pd.Series(data[data['Has_candidate1']==True]['Likes'], index=data['Date'])
    tcandidate2 = pd.Series(data[data['Has_candidate2']==True]['Likes'], index=data['Date'])


    #visualisation
    tcandidate1.plot(figsize=(16,4), label="Candidate1", legend=True)
    tcandidate2.plot(figsize=(16,4), label="Candidate2", legend=True)

    plt.show()

