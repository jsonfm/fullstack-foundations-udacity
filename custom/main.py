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
    html = ""
    for restaurant in restaurants:
        html += F"""
            <div class="card mx-auto my-2 px-4 py-2"  style="max-width: 400px;">
                <div class="row align-items-center">
                    <h4 class="col-8">
                        <a href="/restaurant/view/{restaurant.id}">
                        {restaurant.name}
                        </a>
                    </h4>
                    <div class="col-4">
                        <a class="btn btn-success w-100 mb-2" href="/restaurant/edit/{restaurant.id}">Editar</a>
                        <a class="btn btn-danger w-100" href="/restaurant/edit/{restaurant.id}">Eliminar</a>
                    </div>
                </div>
            </div>
        """
    return render_template("index.html", restaurants=html)


@server.get("/restaurant/edit/:id")
def restaurants(id: str = None):
    print("id: ", id)
    return "Restaurants..."


# Running the server
server.run()