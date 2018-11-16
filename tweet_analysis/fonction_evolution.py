import matplotlib.pyplot as plt
import panda as pd

def retweets_vs_likes (data):
    tfav = pd.Series(data=data['Likes'].values, index=data['Date'])
    tret = pd.Series(data=data['RTs'].values, index=data['Date'])

    # Likes vs retweets visualization:
    tfav.plot(figsize=(16,4), label="Likes", legend=True)
    tret.plot(figsize=(16,4), label="Retweets", legend=True)

    plt.show()


def nombre_tweets_candidats(data, candidat1, candidat2):
    ## Fonction qui détermine le nombre de tweets contenant le nom du candidat 1 et celui du candidat 2
    taille = df.shape(data)[0]
    liste_candidat1=[]
    for k in range(taille):
        if candidat1 in data['tweet_textual_content'][k]:
