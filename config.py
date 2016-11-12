#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = False
SERVER_NAME = 'localhost:5000'
PREFERRED_URL_SCHEME = 'http'

SECRET_KEY = 'this-really-needs-to-be-changed'

SQLALCHEMY_DATABASE_URI = 'postgres-uri-goes-here'
SQLALCHEMY_ECHO = True
DATABASE_CONNECT_OPTIONS = {}
