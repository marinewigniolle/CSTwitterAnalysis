import numpy as np
def maxretweet(data):
    rt_max  = np.max(data['RTs'])
    rt  = data[data.RTs == rt_max].index[0]
    print("The tweet with more retweets is: \n{}".format(data['tweet_textual_content'][rt]))
    print("Number of retweets: {}".format(rt_max))
    print("{} characters.\n".format(data['len'][rt]))

def minretweet(data):
    rt_min  = np.min(data['RTs'])
    rt  = data[data.RTs == rt_min].index[0]
    print("The tweet with more retweets is: \n{}".format(data['tweet_textual_content'][rt]))
    print("Number of retweets: {}".format(rt_max))
    print("{} characters.\n".format(data['len'][rt]))

def recherche_mot(mot,data):
    t = df.shape[data][1]                                   ##Fonction qui renvoie les tweets qui contiennent un mot au choix, par exemple "Macron"
    for k in range t:
        if mot in data['tweet_textual_content'][k]:
            print ("Tweet : \n{}".format(data['tweet_textual_content'][k]))

