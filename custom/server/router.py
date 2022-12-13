class Router:
    """A custom URL router for handle requests and response dynamically"""
    def __init__(self, *args, **kwargs):
        self.routes = {}

    def get_kwargs_from_path(self, path: str):
        """Returns Kwargs contained in an url path and its corresponding index."""
        traces = path.split('/')
        kwargs = {}
        index = 0
        for trace in traces:
            if ":" in trace:
                key = trace.replace(":", "")
                kwargs[key] = index
            index += 1
        return kwargs

    def add(self, method: str = "GET", path: str ="", callback = None):
        """Adds a callback with a respective method on a certain url path."""
        routes = self.routes.get(method, None)
        if routes is None:
            self.routes[method] = {}

        paths = self.routes[method].get(path, None)
        if paths is None:
            kwargs = self.get_kwargs_from_path(path)
            self.routes[method][path] = {
                "callback": callback,
                "kwargs": kwargs
            }

    def fix_path(self, path: str, routes: dict):
        """Fix a url path for understanding dynamic arguments pass."""
        traces = path.split("/")
        for route in routes.keys():
            traces_route = route.split("/")
            if len(traces) == len(traces_route):
                return route
        return "None"

    def get_callback(self, method: str, path: str):
        """Returns the corresponding callback of a url path with an specific method."""
        routes = self.routes.get(method, None)
        if routes is not None:
            fixed_path = self.fix_path(path, routes)
            callback = routes.get(fixed_path, {}).get("callback", None)
            kwargs = routes.get(fixed_path, {}).get("kwargs", None)
            return callback, kwargs
        return None, None

    def get_kwargs_values(self, path, ckwargs):
        """Updates kwargs values with values passed by the url path."""
        traces = path.split("/")
        kwargs = {}
        for varname, index in ckwargs.items():
            kwargs[varname] = traces[index]
        return kwargs

    def execute_callback(self, method: str, path: str):
        """Executes a callback with a certain method on certain url."""
        callback, ckwargs = self.get_callback(method, path)
        if callback is not None:
            kwargs = self.get_kwargs_values(path, ckwargs)
            if len(kwargs) < 1:
                return callback()
            else:
                return callback(**kwargs)
