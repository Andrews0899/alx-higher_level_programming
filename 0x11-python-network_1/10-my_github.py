#!/usr/bin/python3
"""
A Python script that takes your GitHub credentials (username and password) 
and uses the GitHub API to display your id
"""
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://api.github.com/user"
    s = requests.Session()
    s.auth = (argv[1], argv[2])
    req = s.get(url)
    try:
        print('{}'.format(req.json()['id']))
    except:
        print("None")
