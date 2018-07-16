import os
import tornado.httpserver
from tornado.options import define, options
from tornado import gen, web, ioloop
from tornado.httpclient import AsyncHTTPClient

define("port", default=9090, help="run on the given port", type=int)

settings = dict(
    static_path=os.path.dirname(__file__),
    debug=True
)

class TestHandler(web.RequestHandler):
    @web.asynchronous
    @gen.coroutine
    def get(self):
        try:
            # html_fname = os.path.join(template_path, "index.html")
            html_fname = "index.html"
            self.render(html_fname)

        except Exception, e:
            print e


static_path_dir = os.path.dirname(__file__)
handlers = [
    (r'/',TestHandler),
    (r'/(.*)', web.StaticFileHandler, {'path': static_path_dir})
]

url = web.Application(handlers, **settings)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(url, xheaders=True)
    http_server.listen(options.port)
    # http_server.listen(8089,address="192.168.10.204")
    ioloop.IOLoop.instance().start()