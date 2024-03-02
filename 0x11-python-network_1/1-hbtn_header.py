#!/usr/bin/python3
""" response header value """
from urllib import request
from sys import argv

if __name__ == "__main__":

    req = request.request(argv[1])
    with request.urlopen(req) as response:
        print(response.headers["X-request-Id"])
