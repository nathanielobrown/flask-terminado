from terminado import TermSocket, SingleTermManager
from tornado.ioloop import IOLoop
import tornado.web
import tornado.wsgi
import tornado.web


class IndexHandler(tornado.web.RequestHandler):
    def initialize(self, url_prefix):
        self.url_prefix = url_prefix

    def get(self, *args):
        print(args)
        self.render('index.html', url_prefix=self.url_prefix)


class Terminal(object):

    def __init__(self, app=None, url_prefix='/_flask_terminado'):
        assert url_prefix.startswith('/')
        url_prefix = url_prefix.rstrip('/')
        self.url_prefix = url_prefix
        self.app = app
        self.tornado_app = None
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        pass

    def add_terminal(self, route, command, workdir=None, env=None):
        assert route.startswith('/')
        if self.app is None:
            raise Exception("we don't support init_app yet")
        term_manager = SingleTermManager(shell_command=command)
        wrapped_app = tornado.wsgi.WSGIContainer(self.app)
        handlers = [
            ("{}/websocket".format(self.url_prefix),
                TermSocket, {'term_manager': term_manager}),
            (route,
                IndexHandler, {'url_prefix': self.url_prefix}),
            ("{}/(.*)".format(self.url_prefix),
                tornado.web.StaticFileHandler, {'path': '.'}),
            ("/(.*)",
                tornado.web.FallbackHandler, {'fallback': wrapped_app}),
        ]
        self.tornado_app = tornado.web.Application(handlers)

    def run(self, port=8889):
        self.tornado_app.listen(port)
        IOLoop.current().start()


if __name__ == '__main__':
    import flask
    app = flask.Flask(__name__)

    @app.route('/')
    def home():
        return 'home'
    terminal = Terminal(app)
    terminal.add_terminal('/bash', ['ipython'])
    terminal.run()
