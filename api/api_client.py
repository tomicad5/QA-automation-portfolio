import requests


class ApiClient:
    def get(self, url):
        return requests.get(url)

    def post(self, url, data):
        return requests.post(url, json=data)