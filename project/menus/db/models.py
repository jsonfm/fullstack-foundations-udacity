from menus.db import database as db


class Restaurant(db.Model):
    __tablename__ = 'restaurants'
    id = db.Column(
        db.Integer, 
        primary_key = True
    )
    name = db.Column(
        db.String(80),
        nullable=False
    )

    def __repr__(self):
        return f"{self.id} - {self.name}"


class MenuItem(db.Model):
    __tablename__ = 'menuitems'
    id = db.Column(
        db.Integer, 
        primary_key = True
    )
    name = db.Column(
        db.String(80), 
        nullable=False
    )
    course = db.Column(
        db.String(250)
    )
    description = db.Column(
        db.String(250)
    )
    price = db.Column(
        db.String(8)
    )
    restaurant_id = db.Column(
        db.Integer,
        db.ForeignKey('restaurants.id')
    )
    restaurant = db.relationship(Restaurant)
