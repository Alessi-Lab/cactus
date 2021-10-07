from tornado.testing import AsyncTestCase, gen_test

from stringdb.api import StringDB


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

