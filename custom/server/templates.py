from .response import Response
templates = {}


def render_template(filename: str = "", **kwargs):
    """A function for rendering html files on the templates folder settled on the Server."""
    file = templates[filename]
    if len(kwargs) > 0:
        file = file.format(**kwargs)
    response = Response(200, file)
    return response