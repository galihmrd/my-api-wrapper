import os

import requests

from .base64_tools import Base64Tool


class RemoveBGParser:
    def __init__(self, data):
        self.result = data
        self.url = os.getenv("REST_API") + data.get("url")
        self.status = data.get("status")


class RemoveBG(RemoveBGParser):
    def __init__(self, path):
        converted = Base64Tool.image_to_string(path)
        payload = {"image": "data:image/jpeg;base64," + converted, "type": "removebg"}
        api = os.getenv("REST_API")
        try:
            r = requests.post(api + "/removebg", json=payload)
        except Exception as e:
            raise Exception("Error: " + str(e))
        super().__init__(r.json())
