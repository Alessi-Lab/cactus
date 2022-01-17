from tornado.escape import json_decode
from tornado.testing import AsyncTestCase, gen_test

from stringdb.api import StringDB
from proteomicsdb.api import ProteomicsDB

class TestStringDB(AsyncTestCase):
    @gen_test
    def test_get_string_ids(self):
        s = StringDB()
        res = yield s.get_string_ids(["MANEA_MOUSE", "DPP10_MOUSE", "ASIC1_MOUSE"], 10090)

    @gen_test
    def test_get_string_ids(self):
        s = StringDB()
        res = yield s.get_interaction(["MANEA_MOUSE", "DPP10_MOUSE", "ASIC1_MOUSE"], 10090, "physical")

    @gen_test
    def test_enrichment(self):
        s = StringDB()
        res = yield s.get_enrichment(["MANEA_MOUSE"], ["MANEA_MOUSE", "DPP10_MOUSE", "ASIC1_MOUSE"], 10090)
        print(res)

class TestProteomicsDB(AsyncTestCase):
    @gen_test
    def test_get_expression(self):
        p = ProteomicsDB()
        res = yield p.get_expression("P00533")
        print(json_decode(res)["d"]["results"][0])