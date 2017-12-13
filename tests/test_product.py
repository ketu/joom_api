from unittest import TestCase
import joom
import json
from .config import access_token, refresh_token, client_secret, client_id


class TestProduct(TestCase):

    def test_product_retrieve(self):

        client = joom.Client(access_token)
        resp = client.product.disable(parent_sku="8XT3CN4MD7XQ1")

        body = json.loads(resp.text)

        print(body)