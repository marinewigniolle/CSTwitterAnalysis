from textblob import TextBlob

import nltk
nltk.download('punkt')

from textblob import Word


def recuperer_mots_tweet(data,seuil):
    # Fonction renvoyant les mots uniques et lemmatisés d'un ensemble de tweets, et qui sont peu fréquents.

    ## Création de la liste des mots
    L = []

    ## Récupération des mots
    for tweet in data['tweet_textual_content']:
        t=TextBlob(tweet)
        L.append(t.words)

    ## Suppression des mots trop fréquents
    for word in L :
        if L.count(word)>seuil:
            L.delete(word)

    ## Lemmatisation
    for word in L :
        w= Word(word)
        L.append(w.lemmatize())

    return L
