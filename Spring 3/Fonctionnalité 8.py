testimonial = TextBlob("Textblob is amazingly simple to use. What great fun!")

zen = TextBlob("Beautiful is better than ugly. "               "Explicit is better than implicit. "
                "Simple is better than complex.")

for sentence in zen.sentences:
        print(sentence.sentiment)

##Fonction permettant de récupérer les mots uniques et lemmatisés peu fréquents d'un ensemble de tweets
def tweet_extraire(data):
    li = []
    L = []
    for tweet in data['tweet_textual_content']:
        T = TextBlob(tweet)
        li = li.append(T.words)
        ##pour supprimer les mots en trop
        for i in range len(li):
            if li.count(i)
        for word in li:
            w = word.Word
            L =L. append(w.lemmatize)
