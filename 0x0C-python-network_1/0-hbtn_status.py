#!/usr/bin/python3
"""a script that fetches https://intranet.hbtn.io/status"""


def fetch():
    from urllib.request import Request, urlopen
    """gets status"""
    responce = Request("https://intranet.hbtn.io/status")
    with urlopen(responce) as webpage:
        webpage = webpage.read()
        print("Body response:")
        print("\t- type: {}".format(type(webpage)))
        print("\t- content: {}".format(webpage))
        print("\t- utf8 content: {}".format(webpage.decode('utf8')))


if __name__ == "__main__":
    fetch()