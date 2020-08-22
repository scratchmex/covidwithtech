import requests

from pprint import pprint as print


API_KEY = "ad0b17e776d34ffba7dad2b76cdf1b42"

bucket = set()


def fetch():
    url = "http://newsapi.org/v2/top-headlines"
    payload = {
        "apiKey": API_KEY,
        "country": "us",
        "q": "covid",
    }
    response = requests.get(url, params=payload)

    return response.json().get("articles", [])


def get():
    global bucket

    new = fetch()
    bucket.update(new)

    return new
    # urls = set(i.get("url") for i in new)
    # new_urls = urls - bucket
    # bucket |= new_urls

    # return [i for i in new if i.get("url") in new_urls]
