import requests
import os
import pprint
import json
import codecs

# 発行したBearer token
bearer_token = os.environ['BEARER_TOKEN']

# Twitter APIのURL
search_url = "https://api.twitter.com/2/lists/1517926446240768000/tweets"

# 検索クエリ
params = {'max_results': 5, 'expansions': 'attachments.media_keys', 'tweet.fields': 'entities', 'media.fields': 'url'}

headers = {"Authorization": "Bearer {}".format(bearer_token)}

response = requests.request("GET", search_url, headers=headers, params=params)

pprint.pprint(response.json(), indent=4)

with codecs.open('response.json', 'w', 'utf-8') as f:
    json.dump(response.json(), f, ensure_ascii=False, indent=4)