import requests
import os
import json

def returnHTML():
    with open("get/index.json", encoding="utf-8") as f:
        return f.read()

def getData():
    bearer_token = os.environ["BEARER_TOKEN"]

    search_url = "https://api.twitter.com/2/lists/1517926446240768000/tweets"

    params = {"max_results": 5, "expansions": "attachments.media_keys", "tweet.fields": "entities", "media.fields": "url"}

    headers = {"Authorization": "Bearer {}".format(bearer_token)}

    response = requests.request("GET", search_url, headers=headers, params=params)

    # pprint.pprint(response.json(), indent=4)

    with open("response.json", mode="w" ,encoding="utf-8") as f:
        json.dump(response.json(), f, ensure_ascii=False, indent=4)

    with open("get/index.json", mode="w", encoding="utf-8") as f:
        json.dump(response.json(), f, ensure_ascii=False, indent=4)