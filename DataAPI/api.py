import requests

class API:

    def __init__(self):
        pass

    def get_request(self, url):
        return requests.get(url).json()
