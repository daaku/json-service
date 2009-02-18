#!/usr/bin/env python

import wsgiref.handlers
import simplejson
import cgi
import logging

def parse_qs(q):
    try:
        p = cgi.parse_qs(q)
        for each in p:
            if len(p[each]) == 1:
                p[each] = p[each][0]
        return p
    except:
        return {}

def application(environ, start_response):
    headers = {}
    for each in environ:
        if each[:5] == 'HTTP_':
            headers[each[5:].lower()] = environ[each]

    body = environ['wsgi.input'].read()

    response = {
        'method': environ.get('REQUEST_METHOD'),
        'path': environ.get('PATH_INFO'),
        'query_string': environ.get('QUERY_STRING'),
        'content_length': environ.get('CONTENT_LENGTH'),
        'content_type': environ.get('CONTENT_TYPE'),
        'headers': headers,
        'query_params': parse_qs(environ.get('QUERY_STRING')),
        'body': body,
    }
    if response['content_type'] == 'application/x-www-form-urlencoded':
        response['post_params'] = parse_qs(body)
    start_response('200 OK', [('Content-type','application/javascript')])
    return [simplejson.dumps(response, sort_keys=True, indent=4)]
wsgiref.handlers.CGIHandler().run(application)
