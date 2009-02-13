#!/usr/bin/env python
# coding: utf-8

import wsgiref.handlers

def application(environ, start_response):
    start_response('200 OK', [('Content-type','text/html')])
    html = """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">
    <head>
        <meta http-equiv="content-type" content="text/html; charset=utf-8" />
        <title>JSON Services</title>
        <style type="text/css">
            body {
                font-family: "News Gothic MT", Arial;
            }
            h1 {
                color: #0F48B0;
            }
            h2 {
                margin-top: 2em;
            }
            h2 a {
                color: #1695A3;
            }
            h2 a:visited {
                color: #225378;
            }
            h2 a:after {
                content: " »";
            }
        </style>
    </head>
    <body>
        <h1>JSON Services</h1>
        <p>
            Providing JSON Web Services for Unit Testing.
        </p>

        <div class="service">
            <h2><a href="/echo">/echo</a></h2>
            Parsed, structured JSON object representing the HTTP Request.
        </div>

        <div class="service">
            <h2><a href="/time">/time</a></h2>
            Returns the current unix timestamp.
        </div>
    </body>
</html>
"""
    return [html]
wsgiref.handlers.CGIHandler().run(application)
