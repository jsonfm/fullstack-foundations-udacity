import inspect
from .httpbase import CustomHttpServer


class Server:
    def __init__(self, host: str = "0.0.0.0", port: int = 3000):
        self.host = host
        self.port = port
        self._httpserver = CustomHttpServer(host, port)

    def get(self, path, *args, **kwargs):
        def wrapper(callback):
            self._httpserver.router.add(method="GET", path=path, callback=callback)
            return callback
        return wrapper

    def run(self):
        print(f"server running on http://{self.host}:{str(self.port)}")
        self._httpserver.run_forever()