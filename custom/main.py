from server import Server, render_template
from db.models import Restaurant, MenuItem
from db import session


server = Server(
    host="0.0.0.0", 
    port=3000, 
    templates_folder="./templates",
)

@server.get("/")
def home():
    restaurants = session.query(Restaurant).all()
    return render_template("index.html")


@server.get("/restaurants")
def restaurants():
    return "Restaurants..."


# Running the server
server.run()