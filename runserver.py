"""
This script runs the python_webapp_flask application using a development server.
usa el servidor de flask, y es un ambiente de desarrollo/ ya no es de pruebas
"""

from werkzeug import *
from werkzeug.middleware.dispatcher import DispatcherMiddleware  # filtro de solucitudes
from werkzeug.serving import run_simple  # llamador de la funcion

# para pasar parametros , libreria os interactua con las carpetas que tienes en este momento
from os import environ
# identifica el framwork en el cual se corre el código, es importante para la velocidad
from modulos.server import server

from app_admin import app


if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '8095'))
    except ValueError:
        PORT = 8095

    run_simple(HOST, port=PORT, application=DispatcherMiddleware(server))
    #server.run(HOST, PORT)
