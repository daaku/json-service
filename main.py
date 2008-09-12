#!/usr/bin/env python

import wsgiref.handlers

def application(environ, start_response):
    start_response('200 OK', [('Content-type','text/plain')])
    return [str(environ)]
wsgiref.handlers.CGIHandler().run(application)
