import asyncio
import sys

import tornado.httpserver
from tornado.ioloop import IOLoop
from tornado.web import Application

from cactus.handlers import MainHandler, UniprotHandler

settings = {
    #"cookie_secret": "IVM/jkpE+1A4We2P/hVxkHe8EW8mW3TR574hEpCnuGrU3H5trJCSckecA9e2zYthBbI=",
    #"xsrf_cookies": True,
}


if __name__ == "__main__":
    if sys.platform.startswith("win32"):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    app = Application(settings)
    app.add_handlers(r'(localhost|127\.0\.0\.1|62\.75\.251\.157|curtain\.proteo\.info)', [
        (r"/", MainHandler), (r"/uniprot", UniprotHandler)
    ])
    server = tornado.httpserver.HTTPServer(app)
    server.bind(80)

    server.start(0)
    IOLoop.current().start()