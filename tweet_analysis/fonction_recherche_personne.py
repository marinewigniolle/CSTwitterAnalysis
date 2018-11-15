import dataframe as df

def recherche_personne(x,data):
    taille = df.shape(data)[0]
    for k in range(taille):
        if x in data['tweet_textual_content'][k]:
            print("Tweet: \n{}".format(data['tweet_textual_content'][k]))

