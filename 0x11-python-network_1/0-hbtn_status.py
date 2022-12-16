#!/usr/bin/python3
"""What's my status?"""
import urllib.request


if __name__ == "__main__":
    request = urllib.request.Request("http://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(request) as url:
        s = url.read()
        print("Body response:")
        print("\t- type: {}".format(type(s)))
        print("\t- content: {}".format(s))
        print("\t- utf8 content: {}".format(s.decode("utf-8")))
