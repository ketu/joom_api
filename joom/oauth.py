# /usr/bin/env python
# -*- coding:utf8 -*-

import requests
from .settings import BASE_AUTHORIZATION_URL, BASE_ACCESS_TOKEN, BASE_REFRESH_TOKEN
from urllib.parse import urljoin, urlparse, urlencode

class Token(object):

    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret


    def make_authorization_url(self):
        pass

    def fetch_token(self, authorization_code):
        token = self.joom.fetch_token(BASE_ACCESS_TOKEN, code=authorization_code, client_secret=self.client_secret)

    def fetch_token_by_refresh_token(self, refresh_token):
        pass


if __name__ == "__main__":
    token = Token("sdfa", "asdf")
    token.make_authorization_url()
