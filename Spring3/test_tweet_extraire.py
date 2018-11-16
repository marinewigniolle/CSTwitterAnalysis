import pytest
from tweet_extraire import recuperer_mots_tweet

def test_tweet_extraire():
    assert recuperer_mots_tweet() != []
