from http.server import BaseHTTPRequestHandler, HTTPServer
import cgi

def render_form(action="/hello"):
    return f"""
            <form  method="POST" enctype="multipart/form-data" action="{action}">
                <label>Your message</label>
                <input name="message" type="text" placeholder="write here...">
                <button type="submit">Submit</button>
            </form>

    """

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if self.path.endswith("/hello"):
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()

                form = render_form()
                output = f"""
                    <html>
                        <body>
                            <h2>Hello</h2>
                            {form}
                        </body>
                    </html>
                """
                self.wfile.write(bytes(output, "utf-8"))
                return

        except IOError:
            self.send_error(404, f"file not found {self.path}")

    def do_POST(self):
        try:
            self.send_response(301)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            content_type = self.headers.get_content_type()
            boundary = self.headers.get_boundary()
            print("content type: ", content_type)


            ctype, pdict = cgi.parse_header(content_type)
            pdict["boundary"] = str.encode(boundary, "utf-8")

            if ctype == 'multipart/form-data':
                fields = cgi.parse_multipart(self.rfile, pdict)
                message_content = fields.get("message")
                print("type: ", message_content)
            else:
                self.wfile.write(bytes("<html><body>error</body></html>", "utf-8"))
                return

            form = render_form()

            output = f"""
                <html>
                    <body>
                        <h2>What about this: {message_content[0]}</h2>
                        {form}
                    </body>
                </html>
            """
            print("output: ", output)
            self.wfile.write(bytes(output, "utf-8"))
        except Exception as e:
            raise e

def main():
    try:
        port = 8000
        server = HTTPServer(('', port), RequestHandler)
        print(f"server is running on http://localhost:{port}")
        server.serve_forever()
    except KeyboardInterrupt:
        print("bye")


if __name__ == '__main__':
    main()