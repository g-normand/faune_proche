
APP_PATH := $(CURDIR)/faune
ENV_PATH := $(CURDIR)

# For shell to bash to be able to use source.
SHELL = /bin/bash
# Shortcut to set env command before each python cmd.
VENV = source $(ENV_PATH)/bin/activate

# Config is based on two environment files, initalized here.
virtualenv: $(ENV_PATH)/bin/activate

$(ENV_PATH)/bin/activate:
	virtualenv -p /usr/bin/python3.9 $(ENV_PATH)

install: virtualenv
	$(VENV) && pip3 install bottle requests jinja2

start: virtualenv
	$(VENV) && python start-bottle.py
