#!/usr/bin/python3
"""response header value"""

if __name__ == "__main__":
    import urllib.request
    import sys

    request = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(request) as result:
        print(dict(result.headers)['X-Request-Id'])
