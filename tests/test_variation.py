from unittest import TestCase
import joom
import json
from .config import access_token, refresh_token, client_secret, client_id


class TestProduct(TestCase):
    def test_variation_update(self):

        update_data = {
            "shipping_weight": 0.5,
            "sku": "1TR3EL0VB4PA8JN3"
        }
        client = joom.Client(access_token)

        product = client.product.retrieve(id="1494497392564826966-5-1-709-1145779227")

        product = product["Product"]

        resp = client.variation.update(update_data)

        print(resp)