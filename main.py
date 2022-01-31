import asyncio
import os
import sys
from tornado_sqlalchemy import SQLAlchemy
import tornado.httpserver
from tornado.ioloop import IOLoop
from tornado.web import Application, StaticFileHandler
from tornado.options import define, options
from cactus.handlers import MainHandler, UniprotHandler, FileHandler, StringDBGetIDHandler, StringDBInteractionHandler, \
    ProteomicsDBExpressionHandler, InteractomeAtlasHandler

if sys.platform.startswith("win32"):
    database_url = "sqlite:///sql.db?check_same_thread=False"
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
else:
    database_url = "sqlite:////root/cactus/sql.db?check_same_thread=False"

define("port", default=8000, help="Port number")

settings = {
    # "static_path": os.path.join(os.path.dirname(__file__), "static"),
    #"x-header": True
    # "cookie_secret": "IVM/jkpE+1A4We2P/hVxkHe8EW8mW3TR574hEpCnuGrU3H5trJCSckecA9e2zYthBbI=",
    # "xsrf_cookies": True,
}

if __name__ == "__main__":
    tornado.options.parse_command_line()
    rout = os.getenv("handlers_route",
                     r'(production_cactus|production_curtain|localhost|127\.0\.0\.1|62\.75\.251\.157|curtain\.proteo\.info|www\.conducto\.me|conducto\.me)')
    app = Application(db=SQLAlchemy(database_url))
    app.add_handlers(
        rout,
        [
            (r"/", MainHandler),
            (r"/uniprot", UniprotHandler),
            (r"/file_data", FileHandler),
            (r"/string/getid", StringDBGetIDHandler),
            (r"/string/enrichment", StringDBGetIDHandler),
            (r"/string/interaction", StringDBInteractionHandler),
            (r"/proteomics/expression", ProteomicsDBExpressionHandler),
            (r"/interactome/interact", InteractomeAtlasHandler)
            # (r"/static", StaticFileHandler, dict(path=settings['static_path']))
        ])
    server = tornado.httpserver.HTTPServer(app)
    print(options.port)
    server.bind(options.port)

    server.start(1)
    IOLoop.current().start()
