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
            content_type = self.headers.get_content_type()
            boundary = self.headers.get_boundary()
            ctype, pdict = cgi.parse_header(content_type)
            pdict["boundary"] = str.encode(boundary, "utf-8")
            fields = {}
            if ctype == 'multipart/form-data':
                fields = cgi.parse_multipart(self.rfile, pdict)
                fields = multipart_to_dict(fields)

            response = self.router.execute_callback("POST", self.path, response=fields)
            output = response.body
            
            if output is not None:
                self.send_response(response.status)
            else:
                self.send_response(500)
                output = "<html><body>Server Error :(</body></html>"

            if response.status >= 200 and response.status < 300:
                self.send_header("Content-Type", "text/html") 
                self.wfile.write(bytes(output, "utf-8"))

            if response.status >= 300 and response.status < 400:
                self.send_header("Location", response.location)
                
            self.end_headers()

        except Exception as e:
            print("e: ", e)

class CustomHttpServer:
    def __init__(self, host: str = 'localhost', port: int = 3000):
        self.router = Router()
        CustomRequestHandler = partial(RequestHandler, self.router)
        self._server = HTTPServer((host, port), CustomRequestHandler)
    
    def run_forever(self):
        self._server.serve_forever()