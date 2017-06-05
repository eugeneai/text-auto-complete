from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
import os.path
import os
import logging
import sys

logging.basicConfig(level=logging.DEBUG)
logging.debug("Current dir is {}".format(os.getcwd()))


def hello_world(request):
    return Response('Hello {name}!'.format(**(request.matchdict)))


def main():
    config = Configurator()

    config.add_route('hello', '/hello/{name}')
    config.add_view(hello_world, route_name='hello')

    app = config.make_wsgi_app()
    net, port = '0.0.0.0', 8888
    logging.info("Starting server on {}:{}".format(net, port))
    server = make_server(net, port, app)
    server.serve_forever()

main()
quit()
