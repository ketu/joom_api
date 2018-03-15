# /usr/bin/env python
# -*- coding:utf8 -*-

import requests
import random, string
from .settings import BASE_AUTHORIZATION_URL, BASE_ACCESS_TOKEN_URL, BASE_REFRESH_TOKEN_URL
from urllib import parse as urlparse
from .utils import build_response

__all__ = ["Oauth"]


class Oauth(object):
    def __init__(self, client_id, client_secret, redirect_uri):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri

    def make_authorization_url(self, state=None, scope=None):
        u = urlparse.urlparse(BASE_AUTHORIZATION_URL)
        if not state:
            state = "".join(random.sample(string.ascii_letters, 32))
        params = {
            "client_id": self.client_id,
            "redirect_uri": self.redirect_uri,
            "state": state
        }
        if scope:
            params["scope"] = " ".join(scope)

        query = urlparse.urlencode(params)

        url = urlparse.urlunparse((u.scheme, u.netloc, u.path, u.params, query, u.fragment))
        return url, state



    def get_access_token(self, authorization_code):
        params = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "code": authorization_code,
            'grant_type': 'authorization_code',
            'redirect_uri': self.redirect_uri
        }
        r = requests.post(BASE_ACCESS_TOKEN_URL, data=params)
        return build_response(r)

    def get_access_token_by_refresh_token(self, refresh_token):
        params = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "refresh_token": refresh_token,
            'grant_type': 'refresh_token'
        }
        r = requests.post(BASE_REFRESH_TOKEN_URL, data=params)
        return build_response(r)

