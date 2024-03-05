#!/usr/bin/python3
import requests
import json


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "Python script (by /u/your_username) v1.0.0"  # Replace with your Reddit username
    }
    response = requests.get(url, headers=headers)  # Allow redirects for potential API endpoint changes

    if response.status_code == 404:
        return 0

    try:
        results = response.json().get("data")
        return results.get("subscribers")
    except json.JSONDecodeError:
        print("Error: Invalid JSON response received.")
        return None
