#!/usr/bin/python3
"""script that takes your GitHub credentials"""


def github():
    """pass test"""
    from requests import get
    from requests.auth import HTTPBasicAuth
    from sys import argv
    requests = get('https://api.github.com/user',
                   auth=HTTPBasicAuth(argv[1], argv[2])).json()
    print(requests.get('id'))


if __name__ == "__main__":
    github()
