from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from database_setup import MenuItem


def print_db_list(items):
    print("=" * 10)
    for item in items:
        print("item: ", type(item.id) ,item.id, item.name, item.price)


# Create a session
engine = create_engine('sqlite:///restaurantmenu.db')
session = Session(engine)

#Get products
burgers = session.query(MenuItem).filter_by(name="Veggie Burger")
print_db_list(burgers)

# Update Products
burger = session.query(MenuItem).filter_by(id = 20).one()
burger.price = '$9.50'
session.add(burger)
session.commit()

burgers = session.query(MenuItem).filter_by(name="Veggie Burger")
print_db_list(burgers)


# Deleting
        