from flask import render_template
from menus.db import database as db
from menus.db.models import Restaurant, MenuItem
from menus import create_app

app = create_app()

@app.route("/")
def index():
    restaurants = db.session.query(Restaurant).all()
    return render_template("index.html", restaurants=restaurants)

@app.route("/restaurant/<int:restaurant_id>/")
def restaurant_menu(restaurant_id: int):
    restaurant = db.session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = db.session.query(MenuItem).filter_by(restaurant_id=restaurant_id).all()
    return render_template("menu.html", restaurant=restaurant, items=items)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")