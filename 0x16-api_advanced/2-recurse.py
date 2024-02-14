#!/usr/bin/python3
"""recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit."""

import requests


def recurse(subreddit, hot_list=[]):
    """Function to get the number of subscribers of a subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return None
    else:
        for i in range(10):
            hot_list.append(
                response.json().get("data")
                .get("children")[i].get("data").get("title")
            )
        if response.json().get("data").get("after") is not None:
            url = "https://www.reddit.com/r/{}/hot.json?after={}".format(
                subreddit, response.json().get("data").get("after")
            )
            return recurse(subreddit, hot_list)
        return hot_list
