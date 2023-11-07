#!/usr/bin/python3
"""a recursive function that queries the Reddit API and
returns a list containing the titles
of all hot articles for a given subreddit"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "My-User-Agent"}
    params = {"after": after}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        for i in response.json().get("data").get("children"):
            hot_list.append(i.get("data").get("title"))
        after = response.json().get("data").get("after")
        if after is not None:
            recurse(subreddit, hot_list, after)
        return hot_list
    else:
        return None
