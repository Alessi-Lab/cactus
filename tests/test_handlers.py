from unittest import TestCase

import tornado.testing
from tornado.escape import json_encode
from tornado.httpclient import AsyncHTTPClient
from tornado.testing import AsyncTestCase


class TestUniprotHandler(AsyncTestCase):
    @tornado.testing.gen_test
    def test_post(self):
        client = AsyncHTTPClient()
        data = {
            "acc": ["A0JNU3","A1L314","A2A432","A2A4P0","A2A5R2","A2A690","A2A699"]
        }
        response = yield client.fetch(
            "http://62.75.251.157/uniprot",
            method="POST",
            headers={"Content-Type": "application/x-json"},
            body=json_encode(data))
        print(response.body)
