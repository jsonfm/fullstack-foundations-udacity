templates = {}


def render_template(filename: str = ""):
    file = templates[filename]
    return file