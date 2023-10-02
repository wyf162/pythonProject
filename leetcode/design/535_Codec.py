# -*- coding : utf-8 -*-
# @Time: 2022/6/29 21:28
# @Author: yefei.wang
# @File: 535_Codec.py
class Codec:
    tiny_url = "http://tinyurl.com/"

    def __init__(self):
        self.database = {}
        self._id = 0

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self._id += 1
        self.database[self._id] = longUrl
        return self.tiny_url+str(self._id)

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        i = shortUrl.rfind('/')
        _id = int(shortUrl[i+1:])
        return self.database[_id]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
