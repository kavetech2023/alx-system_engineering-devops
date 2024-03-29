#!/usr/bin/python3
"""Get first 10 hot posts"""
import json
import requests


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'u/kavetekevin'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        for i in range(10):
            print(data['data']['children'][i]['data']['title'])
    else:
        print(None)
