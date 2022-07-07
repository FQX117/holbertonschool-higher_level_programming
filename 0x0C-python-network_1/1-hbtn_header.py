#!/usr/bin/python3
"""script that takes in a URL, sends a
request to the URL and displays the value"""


def display():
    from urllib.request import Request, urlopen
    from sys import argv
    """gets status of hbtn intranet"""
    request = Request(argv[1])
    with urlopen(request) as webpage:
        header = webpage.info()
        print(header['X-Request-Id'])


if __name__ == "__main__":
    display()
