#!/usr/bin/python3
"""a recursive function that queries the Reddit API,
parses the title of all hot articles,
and prints a sorted count of given keywords
(case-insensitive, delimited by spaces.
Javascript should count as javascript, but java should not)."""

import requests


def count_words(subreddit, word_list, after=None, word_dict={}):
    url = "https://www.reddit.com/r/{}/hot.json?limit=100".format(subreddit)
    headers = {"User-Agent": "My-User-Agent"}
    params = {"after": after}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        for i in response.json().get("data").get("children"):
            for word in word_list:
                if word.lower() in i.get("data").get("title").lower():
                    if word.lower() not in word_dict:
                        word_dict[word.lower()] = 1
                    else:
                        word_dict[word.lower()] += 1

        after = response.json().get("data").get("after")
        if after is not None:
            count_words(subreddit, word_list, after, word_dict)
        else:
            if len(word_dict) == 0:
                return
            for key, value in sorted(word_dict.items(),
                                     key=lambda x: (-x[1], x[0])):
                print("{}: {}".format(key, value))
