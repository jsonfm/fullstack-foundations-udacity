from functools import partial
import cgi
from http.server import BaseHTTPRequestHandler, HTTPServer
from .router import Router


def multipart_to_dict(multipart):
    data = {}
    for k, v in multipart.items():
        data[k] = v[0]
    return data

class RequestHandler(BaseHTTPRequestHandler):
    def __init__(self, router,  *args, **kwargs):
        self.router = router
        super().__init__(*args, **kwargs)

    def do_GET(self):
        try:
            if not self.path.endswith("/favicon.ico"):
                response = self.router.execute_callback("GET", self.path)
                output = response.body

                if output is not None:
                    self.send_response(200)
                else:
                    self.send_response(404)
                    output = "<html><body>Page Not Found :(</body></html>"

                self.send_header("Content-Type", "text/html")  
                self.end_headers()
                self.wfile.write(bytes(output, "utf-8"))

        except IOError:
            self.send_error(404, f"file not found {self.path}")

    def do_POST(self):
        try:
            fields = {}
            content_type = self.headers.get_content_type()
            boundary = self.headers.get_boundary()
            print("boundary: ", boundary)
            if boundary is not None:
                ctype, pdict = cgi.parse_header(content_type)

                pdict["boundary"] = str.encode(boundary, "utf-8")
        
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    fields = multipart_to_dict(fields)

            response = self.router.execute_callback("POST", self.path, response=fields)
            output = response.body

            if output is None and response.status_code != 302:
                response.status = 500
                output = "<html></p>Error</p></html>"

            self.send_response(response.status)
            
            if response.status >= 200 and response.status < 300:
                self.send_header("Content-Type", "text/html") 
                self.wfile.write(bytes(output, "utf-8"))

            if response.status >= 300 and response.status < 400:
                self.send_header("Location", response.location)

            if response.status >= 500:
                self.send_header("Content-Type", "text/html") 
                self.wfile.write(bytes(output, "utf-8"))

            self.end_headers()

        except Exception as e:
            print("e: ", e)
    
    def do_DELETE(self):
        try:
            print("holy")
        except Exception as e:
            print("e: ", e)

class CustomHttpServer:
    def __init__(self, host: str = 'localhost', port: int = 3000):
        self.router = Router()
        CustomRequestHandler = partial(RequestHandler, self.router)
        self._server = HTTPServer((host, port), CustomRequestHandler)
    
    def run_forever(self):
        self._server.serve_forever()