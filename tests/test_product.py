from unittest import TestCase
import joom
import json

class TestProduct(TestCase):

    def test_product_retrieve(self):
        access_token = 'SEV0001MTUxMTkxNDM0Mnx0X29BYno3ZlNYbjZOZ2ZucE5sbkhNX2dLV3g4NmdWSnNINDlkQmsyLWtiQVdUOW91V2VTOWZpYVFsU3pQeEZYcFNYT2NYLXU0TTZVeG5ITUxyUi11Nng2eXRkV3hYOEtHaU9DZzFVN0RxbFp0MmI4a19pMDFTMFg2elJ2eUR4ck9BOEw2NlNUbWZRdnI0c0s4QlZCOUV1aEpJWTNnNlJrVHNsaGFnPT18KeIHZ5m6AcRRsxtIeJDMGLU6RxAZWvYR6LUnC1PO820='
        refresh_token = 'SEV0001MTQ5MDA4NzQ1OXxiVDJpNUJEVi11Q2F6UnRpdGgxRlFLZzBXdUFYMXBwQjdsUzdQZmJMcmkzVFVrT2pZYXBxcVdXeUgyODVuZ0FYaWp6RWVHVnQzRXRFSkZLTVFBSGdZc2JtM2YyNTRGSG9OOVkyUENlNnozcTFYT2wtUmszbmxxaGxpMmhtUEtpeHJZSEhpUTBKMzBzdFZpcDFSTjlzdFZMdGR2SV84U0RyaVRMeS1sN0dDc3NqU3gxbEVtY0dEWXRrOWVJdkxGQT18YUqNgHfuCgMxWshpqEn445Xj-lUuQ5Ha51GNb2BlXpg='

        client = joom.Client(access_token)
        resp = client.product.disable(parent_sku="8XT3CN4MD7XQ1")

        body = json.loads(resp.text)

        print(body)