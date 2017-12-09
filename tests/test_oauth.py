from unittest import TestCase
import joom
import json

class TestOauth(TestCase):

    def test_make_authorization_url(self):
        token = joom.Token("client_id", "client_secret")
        url, state = token.make_authorization_url()

        print(url)
        print(state)


    def get_access_token(self, authorization_code):
        pass

    def get_access_token_by_refresh_token(self, refresh_token):
        pass