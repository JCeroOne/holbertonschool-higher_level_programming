#!/usr/bin/python3
"""Creates a basic HTTP server."""

import http.server


class SimpleHTTPHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write("Hello, this is a simple API!")

        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({
                "name": "John",
                "age": 30,
                "city": "New York"
            }).encode("utf-8"))

        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({
                "version": "1.0",
                "description": "A simple API built with http.server"
            })).encode("utf-8")

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write("OK")

        else:
            self.send_response(404)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(f"Endpoint '{self.path}' not found on this server!")

    def run(server=http.server.HTTPServer, handler=SimpleHTTPHandler, port=8000):
        httpd = server(("", port), handler)
        print(f"Server listening at 'http://localhost:{port}/'!")
        httpd.serve_forever()
