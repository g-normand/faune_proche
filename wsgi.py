import locale
import sys, os

# Change working directory so relative paths (and template lookup) work again
os.chdir(os.path.dirname(__file__))
sys.path.append(os.path.dirname(__file__))

# ... build or import your bottle application here ...
# Do NOT use bottle.run() with mod_wsgi

import bottle
from bottle_errorsrest import ErrorsRestPlugin

locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')
import faune.home
bottle.install(ErrorsRestPlugin())
application=bottle.default_app()
