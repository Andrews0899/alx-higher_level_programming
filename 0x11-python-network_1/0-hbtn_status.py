#!/usr/bin/python3
"""
A Python script that fetches https://intranet.hbtn.io/status
"""
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        req = response.read()
    print('Body response:')
    print('\t- type: {}'.format(type(req)))
    print('\t- content: {}'.format(req))
    print('\t- utf8 content: {}'.format(req.decode("UTF-8")))
