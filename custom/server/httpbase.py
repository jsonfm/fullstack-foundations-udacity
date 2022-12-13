from functools import partial
from http.server import BaseHTTPRequestHandler, HTTPServer
from .router import Router


class RequestHandler(BaseHTTPRequestHandler):
    def __init__(self, router,  *args, **kwargs):
        self.router = router
        super().__init__(*args, **kwargs)

    def do_GET(self):
        try:
            if not self.path.endswith("/favicon.ico"):
                output = self.router.execute_callback("GET", self.path)

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


class CustomHttpServer:
    def __init__(self, host: str = 'localhost', port: int = 3000):
        self.router = Router()
        CustomRequestHandler = partial(RequestHandler, self.router)
        self._server = HTTPServer((host, port), CustomRequestHandler)
    
    def run_forever(self):
        self._server.serve_forever()