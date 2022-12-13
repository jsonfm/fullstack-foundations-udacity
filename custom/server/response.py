class Response:
    def __init__(self, status=200, body="", location="/"):
        self.status = status
        self.body = body
        self.location = location