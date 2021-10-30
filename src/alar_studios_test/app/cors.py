from typing import Iterable

from flask import Flask, Response, request


def enable_cors(app: Flask):
    @app.after_request
    def print_headers(
            response: Response,
            methods: Iterable = ('GET', 'HEAD', 'POST', 'OPTIONS', 'PUT', 'PATCH', 'DELETE'),
            headers: Iterable = ('Content-Type', 'Authorization')
    ):
        if request.headers.get('Origin') is not None:
            response.headers['Access-Control-Allow-Origin'] = request.headers.get('Origin')
            response.headers['Access-Control-Allow-Methods'] = ','.join(methods)
            response.headers['Access-Control-Allow-Headers'] = ','.join(headers)
        return response
