from textblob import TextBlob
def tweetpos(data):
    li = []
    pos_tweets= []
    for tweet in data['tweet_textual_content']:
        T = TextBlob(tweet)
        li.append(T.sentiment.polarity)
        for i in range len(li):
            if li(i) > 0:
                pos_tweets.append(data['tweet_textual_content'][i])

print("Percentage of positive tweets: {}%".format(len(pos_tweets)*100/len(data['tweet_textual_content'])))

##on fait la même chose avec une polarité nulle pour les tweets neutres et négative pour les tweets négatifs
