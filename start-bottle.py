import locale

from bottle import run

locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')
import faune.home
run(host='localhost', port=8080, debug=True)