#!/usr/bin/python3
"""100-count.py"""
import requests


def count_words(subreddit, word_list, after=None, word_count={}):
    """Function to count the number of times a word appears in the titles
    of the first 100 hot posts listed for a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return None
    if after is None:
        for word in word_list:
            word_count[word] = 0
    for i in range(10):
        title = response.json().get("data").get("children")
        [i].get("data").get("title")
        for word in word_list:
            word_count[word] += title.lower().split().count(word.lower())
    if response.json().get("data").get("after") is not None:
        after = response.json().get("data").get("after")
        url = "https://www.reddit.com/r/{}/hot.json?after={}".format(subreddit,
                                                                     after)
        return count_words(subreddit, word_list, after, word_count)
    else:
        for k, v in word_count.items():
            if v != 0:
                print("{}: {}".format(k, v))
        return word_count
