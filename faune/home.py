from bottle import route, jinja2_view as view, error, static_file, request
import os
import faune.faune_service as faune_service
import logging

PREFIX_ROUTE = ''

@route(PREFIX_ROUTE + '/hello')
def hello():
    return "Hello World!"



@route(PREFIX_ROUTE + '/from_google_maps')
def faune_from_google_maps():
    url = request.query.get('url')
    pas = request.query.get('pas')

    return dict(url=faune_service.get_infos_from_url(url, pas), place=faune_service.get_place(url))


@route(PREFIX_ROUTE + '/')
@view('faune/index.html')
def index():
    return dict()


@error(500)
def error500(error):
    logging.info(error)
    print(error)    
    return 'Oups, une erreur est survenue'

@route(PREFIX_ROUTE + '/static/<filename>')
def server_static(filename):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    return static_file(filename, root=dir_path + '/static')
