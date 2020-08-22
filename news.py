import requests
import json

import phonenumbers as pn
from phonenumbers.phonenumberutil import region_code_for_number
from decouple import config

from utils import get_country

API_KEY = config("NEWS_API_KEY")

with open("news_countries.json") as fp:
    SUPPORTED_COUNTRIES = json.load(fp)

bucket = set()


def fetch(country=None):
    url = "http://newsapi.org/v2/top-headlines"
    payload = {
        "apiKey": API_KEY,
        "country": country if country else "US",
        "q": "covid",
    }
    response = requests.get(url, params=payload)

    return response.json().get("articles", [])


def get(country=None, n=3):
    # global bucket

    new = fetch(country=country)
    # bucket.update(new)

    return new[:n]
    # urls = set(i.get("url") for i in new)
    # new_urls = urls - bucket
    # bucket |= new_urls

    # return [i for i in new if i.get("url") in new_urls]


def action(data):
    country = get_country(data)
    if country not in SUPPORTED_COUNTRIES:
        return {
            "actions": [
                {"say": f"Your country {country} is not supported :c"},
                {
                    "say": "Sorry for this but this are the limitations of the API we are using (https://newsapi.org)"
                },
            ]
        }

    n = 3

    payload = {"actions": [{"say": f"Your 2 letter country code is {country}"}]}

    if "regulations" in data.get("CurrentInput").lower():
        payload["actions"].append(
            {
                "say": "Here you can search for your country specific regulations",
                "say": f"https://www.google.com/search?q=covid+regulations+{country}",
            }
        )

        return payload

    news = get(country=country, n=n)
    if not news:
        payload["actions"] += [{"say": f"We couldn't find any news."}]

        return payload

    payload["actions"] += [{"say": f"Here are the top {n} news"}]
    payload["actions"] += [
        {
            "say": f"Title: {i.get('title', 'No title?. Report this.')}\n\n"
            f"Link: {i.get('url', 'No URL?. Report this.')}"
        }
        for i in news
    ]

    return payload
