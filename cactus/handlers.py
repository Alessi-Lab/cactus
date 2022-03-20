import json
from uuid import uuid4

import bcrypt as bcrypt
from sqlalchemy.exc import NoResultFound
from tornado.escape import json_decode
from tornado.web import RequestHandler
from tornado_sqlalchemy import SessionMixin, as_future

from cactus.database import File
from interactome_atlas.api import InteractomeAtlas
from proteomicsdb.api import ProteomicsDB
from stringdb.api import StringDB
import netphos.api
from uniprot.parser import UniprotSequence, UniprotParser

settings = {}

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


class StringDBGetIDHandler(BaseHandler):
    async def post(self):
        params = json_decode(self.request.body)
        s = StringDB()
        res = await s.get_string_ids(params["id"], params["species"])
        self.write(res)


class StringDBEnrichmentHandler(BaseHandler):
    async def post(self):
        params = json_decode(self.request.body)
        s = StringDB()
        res = await s.get_enrichment(params["study"], params["universe"], params["species"])
        self.write(res)


class StringDBInteractionHandler(BaseHandler):
    async def post(self):
        params = json_decode(self.request.body)
        s = StringDB()
        res = await s.get_interaction(params["id"], params["species"], params["network"])
        self.write(res)


class ProteomicsDBExpressionHandler(BaseHandler):
    async def post(self):
        params = json_decode(self.request.body)
        p = ProteomicsDB()
        res = await p.get_expression(params["id"], params["tissue_type"])
        self.write(res)

class InteractomeAtlasHandler(BaseHandler):
    async def post(self):
        params = json_decode(self.request.body)
        p = InteractomeAtlas()
        res = await p.get_interactions(params["id"])
        self.write(res)

class UniprotHandler(BaseHandler):
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


class FileHandler(SessionMixin, BaseHandler):
    async def put(self):
        with self.make_session() as session:
            hash = ""
            req = json_decode(self.request.body.decode("utf-8"))
            if "password" in req:
                if req["password"]:
                    hash = bcrypt.hashpw(req["password"].encode("utf-8"), bcrypt.gensalt())
            uni = str(uuid4())
            with open(f"files/{uni}.json", "wb") as data:
                data.write(self.request.body)
            f = File(password=hash, filename=uni)

            session.add(f)
            session.commit()
            self.write(uni)

    async def post(self):
        with self.make_session() as session:
            req = json_decode(self.request.body)
            try:
                f = session.query(File).filter(File.filename == req["id"]).one()
                if f.password != "":
                    if req["password"]:
                        if bcrypt.checkpw(req["password"].encode("utf-8"), f.password.encode("utf-8")):
                            with open(f"files/{f.filename}.json", "rb") as d:
                                self.write(d.read())
                        else:
                            self.write({"data": "not found"})
                    else:
                        self.write({"data": "not found"})
                else:
                    with open(f"files/{f.filename}.json", "rb") as d:
                        self.write(d.read())

            except NoResultFound:
                self.write({"data": "not found"})

class NetphosHandler(SessionMixin, BaseHandler):
    def post(self):
        req = json_decode(self.request.body)
        with open("/root/temp/"+req["id"], "wt") as fastaFile:
            fastaFile.write(req["fasta"])
        data = netphos.api.run("/root/api-1.0/ape", "/root/temp/"+req["id"])
        self.write({"data": data})
