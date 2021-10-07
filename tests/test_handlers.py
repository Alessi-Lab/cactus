from functools import partial
from unittest import TestCase
from uuid import uuid4

import requests
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


class TestFileHandler(AsyncTestCase):
    @tornado.testing.gen_test
    def test_post(self):
        with open(r"C:\Users\Toan Phung\Documents\GitHub\curtain\src\assets\DMSO_IN57.txt", "rt") as processed, open(r"C:\Users\Toan Phung\Documents\GitHub\curtain\src\assets\Rawdata.txt", "rt") as raw:
            res = requests.put("http://localhost:8000/file_data", data=json_encode({"password": "test", "processed": processed.read(),
               "raw": raw.read()}), headers={"Content-Type": "multiplepart/form-data"})

        print(res)