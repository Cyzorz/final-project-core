from ratelimit import limits
import json
import requests
import config

class API:
    @limits(calls=config.REQUESTS_PER_COOLDOWN, period=config.API_COOLDOWN)
    def call(query, url, content_type):
        headers = {'Content-type': content_type}
        data = json.dumps(query)
        p = requests.post(url, data=data, headers=headers)
        return p