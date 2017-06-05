from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
import os.path
import os
import logging
import sys
import glob

logging.basicConfig(level=logging.DEBUG)

PWD = os.getcwd()


def templ(name):
    return os.path.join(PWD, "indripress", name + ".pt")


logging.debug("Current dir is {}".format(os.getcwd()))


def main_page(request):
    return {"title": "Диагноз"}


def hello_world(request):
    return Response('Hello {name}!'.format(**(request.matchdict)))


def helm(request):
    return [
        {"name": 'James Harden'},
        {"name": 'Фалалеев'},
        {"name": 'Jenniffer Caffey'},
        {"name": 'Paul Hollen'},
        {"name": 'Isabel Lenzi'},
        {"name": 'Rebecka Kennell'},
        {"name": 'Collette Janis'},
        {"name": 'Bryon Kawamoto'},
        {"name": 'Jerald Mozingo'},
        {"name": 'Carlena Bachelor'},
        {"name": 'Jacinta Diver'},
        {"name": 'Cameron Libbey'},
        {"name": 'Romana Matsunaga'},
        {"name": 'Laurette Ernst'},
        {"name": 'Gilma Groom'},
        {"name": 'Lewis Gillis'},
        {"name": 'Weston Defoor'},
        {"name": 'Alejandrina Simmer'},
        {"name": 'Alejandra Helbing'},
        {"name": 'Yvette Fielding'},
        {"name": 'Shirely Besaw'},
        {"name": 'Laurel Dafoe'},
        {"name": 'Shantel Calley'},
        {"name": 'Aleta Bolyard'},
        {"name": 'Tuyet Ybarbo'},
        {"name": 'Christy Voris'},
        {"name": 'Hilda Hamlett'},
        {"name": 'Ying Tefft'},
        {"name": 'Lilliana Fulford'},
        {"name": 'Jama Brough'},
        {"name": 'Minerva Bixby'},
        {"name": 'Jacquelin Lauber'},
        {"name": 'Lanette Hoke'},
        {"name": 'Virgil Roehr'},
        {"name": 'Melodi Rathburn'},
        {"name": 'Tressa Cade'},
        {"name": 'Florentina Seigel'},
        {"name": 'Santina Maust'},
        {"name": 'Sean Spidle'},
        {"name": 'Henrietta Murtagh'},
        {"name": 'Matilde Tynan'},
        {"name": 'Claude Putman'},
        {"name": 'Ardell Castiglia'},
        {"name": 'Alona Mally'},
        {"name": 'Elizabet Gebhart'},
        {"name": 'Maye Wilken'},
        {"name": 'Xenia Gin'},
        {"name": 'Edith Schebler'},
        {"name": 'Brianna Repka'},
        {"name": 'Marcella Thronson'},
        {"name": 'Theresia Provenzano'}
    ]


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
