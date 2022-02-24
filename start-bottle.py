import locale
from bottle import run
import faune.home

locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')
run(host='localhost', port=8080, debug=True)
