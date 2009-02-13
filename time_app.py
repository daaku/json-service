#!/usr/bin/env python

import wsgiref.handlers
import simplejson
import time


def application(environ, start_response):
    start_response('200 OK', [('Content-type','application/javascript')])
    return [str(int(time.time()))]
wsgiref.handlers.CGIHandler().run(application)
