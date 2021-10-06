import asyncio
import os
import sys

import tornado.httpserver
from tornado.ioloop import IOLoop
from tornado.web import Application, StaticFileHandler
from tornado.options import define, options
from cactus.handlers import MainHandler, UniprotHandler

define("port", default=8000, help="Port number")

settings = {
    # "static_path": os.path.join(os.path.dirname(__file__), "static"),
    #"x-header": True
    # "cookie_secret": "IVM/jkpE+1A4We2P/hVxkHe8EW8mW3TR574hEpCnuGrU3H5trJCSckecA9e2zYthBbI=",
    # "xsrf_cookies": True,
}

if __name__ == "__main__":
    tornado.options.parse_command_line()
    if sys.platform.startswith("win32"):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    app = Application(settings)
    app.add_handlers(
        r'(localhost|127\.0\.0\.1|62\.75\.251\.157|curtain\.proteo\.info)',
        [
            (r"/", MainHandler),
            (r"/uniprot", UniprotHandler),
            # (r"/static", StaticFileHandler, dict(path=settings['static_path']))
        ])
    server = tornado.httpserver.HTTPServer(app)
    print(options.port)
    server.bind(options.port)

    server.start(1)
    IOLoop.current().start()
