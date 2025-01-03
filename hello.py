# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "requests",
# ]
# ///
import requests


def main():
    print(requests.get("https://httpbin.org/ip").text)


if __name__ == "__main__":
    main()
