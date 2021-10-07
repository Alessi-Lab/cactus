import bcrypt as bcrypt
from tornado.escape import json_decode
from tornado.web import RequestHandler
from tornado_sqlalchemy import SessionMixin, as_future

from cactus.database import File
from uniprot.parser import UniprotSequence, UniprotParser

class BaseHandler(RequestHandler):
    def set_default_headers(self):
        self.set_header("access-control-allow-origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'GET, PUT, DELETE, OPTIONS')
        self.set_header("Access-Control-Allow-Headers", "access-control-allow-origin,authorization,content-type")

    def options(self):
        self.set_status(204)
        self.finish()


class MainHandler(BaseHandler):
    def get(self):
        self.write("Hello, world")


class UniprotHandler(BaseHandler):
    def post(self):
        params = json_decode(self.request.body)
        acc = []

        for a in params["acc"]:
            u = UniprotSequence(a, True)
            acc.append(str(u))
        print(acc)
        parser = UniprotParser(acc)
        data = ""
        for p in parser.parse(format="tab", method="post"):
            data += p
        print(data)
        self.write(data)


class FileHandler(SessionMixin, BaseHandler):
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