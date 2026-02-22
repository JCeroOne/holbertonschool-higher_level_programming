#!/usr/bin/python3
"""Defines the fetch_and_print_posts and fetch_and_save_posts functions."""

import requests as req
import csv

def fetch_and_print_posts():
    """Gets all the posts from JSONPlaceholder and prints them."""
    
    res = req.get("https://jsonplaceholder.typicode.com/posts")
    print(f"Status Code: {res.status_code}")
    
    if res.status_code == 200:
        data = res.json()
        for post in data:
            print(post["title"])


def fetch_and_save_posts():
    """Gets all the posts from JSONPlaceholder ans saves them to posts.csv"""

    res = req.get("https://jsonplaceholder.typicode.com/posts")

    if res.status_code == 200:
        data = res.json()
        with open("posts.csv", "w") as csv:
            writer = csv.DictWriter(csv, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
