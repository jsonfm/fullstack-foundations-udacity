import os
from .httpbase import CustomHttpServer
from .templates import templates


class Server:
    """Custom HTTP server with cool API for decorators."""
    def __init__(self, host: str = "0.0.0.0", port: int = 3000, templates_folder: str = None):
        self.host = host
        self.port = port
        self._httpserver = CustomHttpServer(host, port)
        self.templates_folder = templates_folder
        self.templates = templates
        self.load_templates(self.templates_folder)

    def get(self, path, *args, **kwargs):
        """Establishes a callback for reponse to a GET request."""
        def wrapper(callback):
            self._httpserver.router.add(method="GET", path=path, callback=callback)
            return callback
        return wrapper

    def post(self, path, *args, **kwargs):
        """Establishes a callback for reponse to a POST request."""
        def wrapper(callback):
            self._httpserver.router.add(method="POST", path=path, callback=callback)
            return callback
        return wrapper

    def delete(self, path, *args, **kwargs):
        """Establishes a callback for reponse to a DELETE request."""
        def wrapper(callback):
            self._httpserver.router.add(method="DELETE", path=path, callback=callback)
            return callback
        return wrapper


    def run(self):
        """Executes the server on a blocking thread"""
        print(f"server running on http://{self.host}:{str(self.port)}")
        self._httpserver.run_forever()
    
    def load_templates(self, path: str):
        """Loads html files to be rendered."""
        for file in os.listdir(path):
            filepath = os.path.join(path, file)
            opened = open(filepath)
            readed = opened.read()
            self.templates[file] = readed
            opened.close()
