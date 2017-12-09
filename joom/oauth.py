# /usr/bin/env python
# -*- coding:utf8 -*-

from requests_oauthlib import OAuth2Session
from .settings import BASE_AUTHORIZATION_URL, BASE_URL

print(BASE_AUTHORIZATION_URL)
class Token(object):

    def __init__(self, client_id, client_secret):
        self.client_id =client_id
        self.client_secret = client_secret

        self.joom = OAuth2Session(client_id=self.client_id)

    def make_authorization_url(self, ):
        return self.joom.authorization_url(BASE_AUTHORIZATION_URL)


    def fetch_token(self):
        pass


if __name__ == "__main__":
    token = Token("sdfa", "asdf")
    token.make_authorization_url()