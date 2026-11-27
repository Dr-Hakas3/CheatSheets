## putリクエストを受け付ける簡易サーバ
import os
from http.server import HTTPServer, SimpleHTTPRequestHandler

class MyHTTPRequestHandler(SimpleHTTPRequestHandler):
    def do_PUT(self):
        length = int(self.headers['Content-Length'])
        path = self.translate_path(self.path)
        with open(path, 'wb') as f:
            f.write(self.rfile.read(length))
        self.send_response(201, "Created")
        self.end_headers()

def run(server_class=HTTPServer, handler_class=MyHTTPRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
