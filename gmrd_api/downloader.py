import os
from requests import Session
from .exceptions import *



class InfoParser:
    def __init__(self, data):
        if data.get("data").get("type"):
            self.artist = data.get("data").get("artists")
            self.title = data.get("data").get("title")
            self.duration = data.get("data").get("duration")
            self.thumbnail = data.get("data").get("thumbnail")
            self.url = data.get("data").get("url")
            self.status = data.get("status")
        else:
            self.results = data.get("data")
            self.audio_url = data.get("data").get("audio_url")
            self.author = data.get("data").get("author")
            self.caption = data.get("data").get("caption")
            self.latency = data.get("data").get("latency")
            self.platform = data.get("data").get("platform")
            self.thumbnail = data.get("data").get("thumbnail")
            self.url = data.get("data").get("url")
            self.views = data.get("data").get("views")
            self.status = data.get("status")


class GetInfo(InfoParser):
    def __init__(self, url):
        payload = {"url": url}
        sess = Session()
        api = os.getenv("REST_API")
        try:
            response = sess.post(api + "/api", json=payload)
            if response.status_code == 200:
                data = response.json()
            else:
                raise NoResultFound("Error, status code:" + str(response.status_code))
        except Exception as e:
            raise NoResultFound(e)
        super().__init__(data)


class SaveFile:
    def __init__(self, url: str, path: str):
        try:
            r = Session().get(url, allow_redirects=True)
            content_type = r.headers["Content-Type"]
            if content_type.split("/")[0] == "image":
                extension = ".jpg"
            elif content_type.split("/")[0] == "video":
                extension = ".mp4"
            elif content_type.split("/")[0] == "audio":
                extension = ".mp3"
            else:
                if r.headers.get("x-cdn-item-type") == "video":
                    extension = ".mp4"
                else:
                    extension = ".jpg" if not "mp4" in url else ".mp4"
            open(path + extension, 'wb').write(r.content)
        except Exception as e:
            raise DownloadError(f"Failed to download file {e}")
