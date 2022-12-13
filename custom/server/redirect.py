from .response import Response

def redirect(path: str = "/"):
    response = Response(302, "<p>redirecting</p>", path)
    return response