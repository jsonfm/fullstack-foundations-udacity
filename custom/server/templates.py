templates = {}


def render_template(filename: str = "", **kwargs):
    """A function for rendering html files on the templates folder settled on the Server."""
    file = templates[filename]
    file = file.format(**kwargs)
    return file