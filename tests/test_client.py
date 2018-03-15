from unittest import TestCase
import joom
from .config import access_token, refresh_token, client_secret, client_id


class TestClient(TestCase):
    def test_client(self):
        client = joom.Client(access_token)
