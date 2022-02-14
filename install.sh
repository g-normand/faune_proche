#!/bin/sh
PROJECT_ROOT=$(pwd)

cd /tmp
wget --no-check-certificate https://pypi.python.org/packages/source/v/virtualenv/virtualenv-15.0.0.tar.gz
tar -vxf virtualenv-15.0.0.tar.gz
cd virtualenv-15.0.0/
python virtualenv.py  -p python3 --no-site-package $PROJECT_ROOT
cd $PROJECT_ROOT
source bin/activate
pip install bottle requests jinja2
