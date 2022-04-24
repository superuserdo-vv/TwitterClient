import requests
import os

bearer_token = os.environ['BEARER_TOKEN']

# search_url = "https://api.twitter.com/2/users/1511703981655212035/tweets"
search_url = "https://api.twitter.com/2/lists/1517926446240768000/tweets"

params = {'max_results': 10}

def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers

def connect_to_endpoint(url, headers, params):
    has_next = True
    c = 0
    result = []
    while has_next:
        response = requests.request("GET", search_url, headers=headers, params=params)
        if response.status_code != 200:
            raise Exception(response.status_code, response.text)

        response_body = response.json()
        result += response_body['data']

        rate_limit = response.headers['x-rate-limit-remaining']
        print('Rate limit remaining: ' + rate_limit)

        c = c + 1
        has_next = ('next_token' in response_body['meta'].keys() and c < 300)

    return result
