from unittest import TestCase
import joom
import json
from .config import access_token, refresh_token, client_secret, client_id


class TestOauth(TestCase):
    def test_make_authorization_url(self):
        token = joom.Oauth("dbad2db62b430f53", "73dc10dec5ec9a2fbaa4a038646c7ccf", "http://127.0.0.1")
        url, state = token.make_authorization_url()

        print(url)
        print(state)
