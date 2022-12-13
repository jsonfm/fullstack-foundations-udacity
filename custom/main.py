from server import Server

server = Server(host="0.0.0.0", port=3000)

@server.get("/")
def home():
    return "Home"


@server.get("/restaurants")
def restaurants():
    return "Restaurants..."


# Running the server
server.run()