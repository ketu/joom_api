from unittest import TestCase
import joom
import json

class TestOauth(TestCase):

    def test_make_authorization_url(self):
        token = joom.Token("dbad2db62b430f53", "73dc10dec5ec9a2fbaa4a038646c7ccf")
        url, state = token.make_authorization_url()

        print(url)
        print(state)



    def test_get_access_token(self, authorization_code):
        pass



    def test_get_access_token_by_refresh_token(self, refresh_token):

        refresh_token = "SEV0001MTUxMjAyNjQyN3xPTmM0eTdpQk55VmRiMTBZU01GZW0tMTJnUDZOVUJCQVRNRDFZbFIxZUpjUWhXUXNReUhjWmJ0a2kxYWM4b0d3enZ1dXc0eFVtQkU0ckxUdkU5R3liWTNDZ0tZWVN6ZnBHSTY0OGxnLXA2eTNBQ21jOWlOdEY3WjI1MnVmLXFfRU9VeXAwZVBETHdtNFY0U0Q1N0FKbHBGbTdXWTFxMnJaV3h3dFpDOHQ2N2xIdzUwNFBERjhKZmEzcnVpaUM1amktdz09fDpU6p8y7UmsLlnQnyHt4GnJkFl2lwtb1-DmwNNJB_ad"


