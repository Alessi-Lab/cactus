import bcrypt as bcrypt
from tornado.escape import json_decode
from tornado.web import RequestHandler
from tornado_sqlalchemy import SessionMixin, as_future

from cactus.database import File
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


class FileHandler(SessionMixin, RequestHandler):
    async def put(self):
        with self.make_session() as session:
            hash = ""
            req = json_decode(self.request.body.decode("utf-8"))
            if "password" in req:
                if req["password"]:
                    hash = bcrypt.hashpw(req["password"].encode("utf-8"), bcrypt.gensalt())

            count = await as_future(session.query(File).count)
            print(count)
            f = File(password=hash, filename="test.txt")

            session.add(f)
            session.commit()
            count = await as_future(session.query(File).count)
            print(count)
            print(f)
            self.write(str(count))