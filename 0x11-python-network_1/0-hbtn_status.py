#!/usr/bin/python3
"""What's my status?"""
import urllib.request


if __name__=="__main__":
    request = urllib.request.Request("http://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(request) as url:
        s = url.read()
        req = "Body response:\n\-t type: {}\n\t- content: {}\n\t- utf8 content: {}"
        print(req.format(type(s), s, s.decode('utf-8')))
