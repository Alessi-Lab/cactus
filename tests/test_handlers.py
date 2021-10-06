from functools import partial
from unittest import TestCase
from uuid import uuid4

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
        client = AsyncHTTPClient()
        data = {
            "acc": ["A0JNU3","A1L314","A2A432","A2A4P0","A2A5R2","A2A690","A2A699"]
        }
        boundary = uuid4().hex
        headers = {"Content-Type": "multipart/form-data"}
        producer = partial(multipart_producer, boundary, filenames)
        response = yield client.fetch(
            "http://localhost:8888/post",
            method="POST",
            headers=headers,
            body_producer=producer,
        )
        response = yield client.fetch(
            "http://localhost:8000/file_data",
            method="POST",
            headers={"Content-Type": "multiplepart/form-data"},
            files={"processed": r"C:\Users\Toan Phung\Documents\GitHub\curtain\src\assets\DMSO_IN57.txt",
                   "raw": r"C:\Users\Toan Phung\Documents\GitHub\curtain\src\assets\Rawdata.txt"})
        print(response.body)