#!/usr/bin/python3
"""send a post requestwith mail"""
from urllib import request, parse
from sys import argv

if __name__ == "__main__":
    values = {'email': argv[2]}
    data = parse.urlencode(values)
    data = data.encode("ascii")
    req = request.Request(argv[1], data)
    with request.urlopen(req) as response:
        print(response.read().decode("utf-8"))
