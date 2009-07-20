#!/usr/bin/env python

import wsgiref.handlers
import cgi
import time

def application(environ, start_response):
    seconds = float(cgi.parse_qs(environ.get('QUERY_STRING'))['seconds'][0])
    time.sleep(seconds)
    start_response('200 OK', [('Content-type','text/plain')])
    return ['Slept for %i' % seconds]
wsgiref.handlers.CGIHandler().run(application)
