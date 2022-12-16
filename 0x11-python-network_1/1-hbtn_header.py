#!/usr/bin/python3
"""Response header value"""
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as url:
        s = url.getheader('-X-Request-Id')
        print("{}".format(s))
