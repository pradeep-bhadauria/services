#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = False
SERVER_NAME = 'localhost:5000'
PREFERRED_URL_SCHEME = 'http'

SECRET_KEY = 'this-really-needs-to-be-changed'

SQLALCHEMY_DATABASE_URI = 'postgres://jcepytxffjskun:heHyQX9CwinC9EpJCZIceXAGR4@ec2-54-163-239-63.compute-1.amazonaws.com:5432/d241q24dttbkg1'
SQLALCHEMY_ECHO = True
DATABASE_CONNECT_OPTIONS = {}