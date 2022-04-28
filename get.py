import requests
import os
import pprint
import json
import codecs

def htmlReturn():
    with open("index.html") as f:
        return f.read()

def main():
    bearer_token = os.environ["BEARER_TOKEN"]

    search_url = "https://api.twitter.com/2/lists/1517926446240768000/tweets"

    params = {"max_results": 10, "expansions": "attachments.media_keys", "tweet.fields": "entities", "media.fields": "url"}

    headers = {"Authorization": "Bearer {}".format(bearer_token)}

    response = requests.request("GET", search_url, headers=headers, params=params)

    pprint.pprint(response.json(), indent=4)

    with codecs.open("response.json", "w", "utf-8") as f:
        json.dump(response.json(), f, ensure_ascii=False, indent=4)

    with codecs.open("get/index.html", "w", "utf-8") as f:
        json.dump(response.json(), f, ensure_ascii=False, indent=4)