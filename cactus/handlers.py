from tornado.escape import json_decode
from tornado.web import RequestHandler

from uniprot.parser import UniprotSequence, UniprotParser


class MainHandler(RequestHandler):
    def get(self):
        self.write("Hello, world")


class UniprotHandler(RequestHandler):
    def post(self):
        params = json_decode(self.request.body)
        acc = []
        for a in params["acc"]:
            u = UniprotSequence(a, True)
            acc.append(str(u))

        parser = UniprotParser(acc)
        data = ""
        for p in parser.parse(format="tab", method="post"):
            data += p
        self.write(data)
