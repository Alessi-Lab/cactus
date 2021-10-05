import asyncio
import sys

from tornado.ioloop import IOLoop
from tornado.web import Application, RequestHandler
import os

class MainHandler(RequestHandler):
    def get(self):
        self.write("Hello, world")

if __name__ == "__main__":
    if sys.platform.startswith("win32"):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    app = Application([
        (r"/", MainHandler)
    ])
    app.listen(8080)
    IOLoop.current().start()