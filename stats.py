import requests
import json
import urllib.parse

from utils import get_country

# Data saved at 2020-08-22T22:24:47Z
# _data = requests.get("https://api.covid19api.com/countries").json()
# SUPPORTED_COUNTRIES = {i["ISO2"]: i["Slug"] for i in _data}
with open('stats_countries.json') as fp:
    SUPPORTED_COUNTRIES = json.load(fp)


def fetch(country=None):

    url = f"https://api.covid19api.com/summary"
    r = requests.get(url)
    data = r.json()

    for i in data["Countries"]:
        if i["CountryCode"] == country:
            return i

    return {}


def get(country=None):
    return fetch(country=country)


def action(data):
    country = get_country(data)

    api_limitations_msg = {
        "say": "Sorry for this but this are the limitations of the API we are using (https://covid19api.com)"
    }

    if country not in SUPPORTED_COUNTRIES.keys():
        return {
            "actions": [
                {"say": f"Your country {country} is not supported :c"},
                api_limitations_msg,
            ]
        }

    status_wanted = data.get("Field_stat_Value")
    if status_wanted and status_wanted == "active":
        google_query = urllib.parse.urlencode(
            {"q": data.get("CurrentInput") + f" {country}"}
        )
        return {
            "actions": [
                {"say": f"We don't have that information :s"},
                api_limitations_msg,
                {
                    "say": f"We encourage you to search it on Google: https://www.google.com/search?{google_query}"
                },
            ]
        }

    country_data = get(country=country)

    country_name = country_data["Country"]
    confirmed = country_data["TotalConfirmed"]
    recovered = country_data["TotalRecovered"]
    deaths = country_data["TotalDeaths"]

    payload = {
        "actions": [
            {"say": f"Your 2 letter country code is {country}"},
            {
                "say": f"For your country ({country_name}) here are the stats:\n\n"
                f"- total cases confirmed: {confirmed:,}\n"
                f"- total recovered: {recovered:,}\n"
                f"- total deaths: {deaths:,}"
            },
        ]
    }

    return payload
