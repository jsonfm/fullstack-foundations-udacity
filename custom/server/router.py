class Router:
    def __init__(self, *args, **kwargs):
        self.routes = {}

    def add_get(self, path: str, callback):
        self.routes["GET"] = {
            path: callback
        }

    def get_post(self, path: str, callback):
        self.routes["POST"] = {
            path: callback
        }
    
    def add(self, method: str = "GET", path: str ="", callback = None):
        routes = self.routes.get("GET", None)
        if routes is None:
            self.routes[method] = {}
        self.routes[method][path] = callback

    
    def get_callback(self, method: str, path: str):
        routes = self.routes.get(method, None)
        if routes is not None:
            callback = routes.get(path, None)
            return callback

    def execute_callback(self, method: str, path: str) -> str:
        callback = self.get_callback(method, path)
        # args, kwargs = self.get_callback_argunments()
        if callback is not None:
            return callback()
