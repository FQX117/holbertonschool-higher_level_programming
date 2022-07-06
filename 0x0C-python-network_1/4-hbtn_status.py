#!/usr/bin/python3
"""script that fetches"""


def status():
    """pass test"""
    from requests import get
    request = get("https://intranet.hbtn.io/status")
    text = request.text
    print("Body response:")
    print("\t- type: {}".format(type(text)))
    print("\t- content: {}".format(text))


if __name__ == "__main__":
    status()
