#!/usr/bin/python3
"""script that fetches"""


def error():
    """pass test"""
    from requests import get
    from sys import argv
    request = get(argv[1])
    if request.status_code >= 400:
        print("Error code: {}".format(request.status_code))
    else:
        print(request.text)


if __name__ == "__main__":
    error()
