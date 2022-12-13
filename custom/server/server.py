import os
from .httpbase import CustomHttpServer
from .templates import templates


class Server:
    def __init__(self, host: str = "0.0.0.0", port: int = 3000, templates_folder: str = None):
        self.host = host
        self.port = port
        self._httpserver = CustomHttpServer(host, port)
        self.templates_folder = templates_folder
        self.templates = templates
        self.load_templates(self.templates_folder)

    def get(self, path, *args, **kwargs):
        def wrapper(callback):
            self._httpserver.router.add(method="GET", path=path, callback=callback)
            return callback
        return wrapper

    def run(self):
        print(f"server running on http://{self.host}:{str(self.port)}")
        self._httpserver.run_forever()
    
    def load_templates(self, path: str):
        for file in os.listdir(path):
            filepath = os.path.join(path, file)
            opened = open(filepath)
            readed = opened.read()
            self.templates[file] = readed
            opened.close()
