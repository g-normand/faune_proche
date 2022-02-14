# faune_proche

Récupération des données de Faune-France près d'un lieu google maps.

Utilisation de Bottle (https://bottlepy.org/docs/dev/)

Tout passe par le WSGI
Pour Alwaysdata, c'est dans /admin/config/uwsgi
```
chdir = /home/faune/www
wsgi-file = /home/faune/www/wsgi.py
``` 

Sinon faire:
```
make start
```


Pour l'installation:
```
$ git clone git@github.com:g-normand/faune_proche.git
$ cd faune_proche
$ make install
``` 
