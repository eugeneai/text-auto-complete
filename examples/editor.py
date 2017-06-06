from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
import os.path
import os
import logging
import glob
import pprint
from isu.autocomplete import analysis

logging.basicConfig(level=logging.DEBUG)

PWD = os.getcwd()


def templ(name):
    return os.path.join(PWD, "indripress", name + ".pt")


logging.debug("Current dir is {}".format(os.getcwd()))

HELM = analysis.main()


def main_page(request):
    return {"title": "Диагноз"}


def hello_world(request):
    return Response('Hello {name}!'.format(**(request.matchdict)))


def helm(request):
    data = request.GET
    # diag = data["diag"]
    mkb10 = data["mkb10"]
    pattern = data["pattern"]
    prf = pattern.strip().split(" ")
    rc = HELM.query(mkb10=mkb10, prefixes=prf)
    rc = [{"name": " ".join(val)} for val in rc]
    logging.debug("Prefix = '{}', mkb10='{}'".format(pattern, mkb10))
    logging.debug(pprint.pformat(rc))
    return rc


def main():
    config = Configurator(settings={
        'pyramid.reload_templates': True,
        'pyramid.debug_templates': True
    })

    config.add_route('hello', '/hello/{name}')
    config.add_route('editor', '/')
    config.add_route('helm', '/api/helm')
    config.add_view(hello_world, route_name='hello')
    config.add_view(helm, route_name='helm',
                    renderer='json')
    config.add_view(main_page, route_name='editor',
                    renderer=templ("index"))
    config.include('pyramid_debugtoolbar')
    config.include('pyramid_chameleon')

    statics = glob.glob("*/*/")
    for st in statics:
        path = os.path.join(PWD, st)
        name = st.replace("indripress/", '').replace("/", '')
        logging.debug("path = {}, name = {}".format(path, name))
        config.add_static_view(name=name, path=path)

    config.add_static_view(name="css", path=os.path.join(PWD, 'css'))
    config.add_static_view(name="js", path=os.path.join(PWD, 'js'))

    app = config.make_wsgi_app()
    net, port = '0.0.0.0', 8888
    logging.info("Starting server on {}:{}".format(net, port))
    server = make_server(net, port, app)
    server.serve_forever()

main()
quit()
