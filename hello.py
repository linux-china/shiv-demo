# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "requests",
# ]
# ///
import sys

import requests


def main():
    print(requests.get("https://httpbin.org/ip").text)
    print(sys.version_info)


if __name__ == "__main__":
    main()