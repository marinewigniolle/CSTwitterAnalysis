from textblob import TextBlob

import nltk
nltk.download('punkt')

wiki = TextBlob("Python is a high-level, general-purpose programming language")


zen = TextBlob("Beautiful is better than ugly."
               "Explicit is better than implicit."
               "Simple is better than complex.")

for sentence in zen.sentences :
    print(sentence.sentiment)

