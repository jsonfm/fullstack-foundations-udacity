from server import Server, render_template, redirect
from db.models import Restaurant, MenuItem
from db import session
from renders import render_restaurant_list, render_restaurant_edit


server = Server(
    host="0.0.0.0", 
    port=3000, 
    templates_folder="./templates",
)


@server.get("/")
def home():
    restaurants = session.query(Restaurant).all()
    html = render_restaurant_list(restaurants)
    return render_template("index.html", restaurants=html)


@server.get("/restaurant/edit/:id")
def restaurants(id: str = None):
    restaurant = session.query(Restaurant).filter_by(id=id).first()
    html = render_restaurant_edit(restaurant)
    return render_template("restaurant_edit.html", restaurant=html)


@server.get("/restaurants/create")
def restaurant_create_view():
    return render_template("restaurant_create.html")


@server.post("/restaurants/create/")
def create_restaurant(response):
    print("creating a restaurant: ", response, type(response))
    return redirect("/")

# Running the server
server.run()