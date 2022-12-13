
def render_restaurant_list(restaurants: list):
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
    return html

def render_restaurant_edit(restaurant):
    html = f"""
        <div class="card mx-auto px-4 py-4" style="max-width: 500px">
            <form method="POST" action="/restaurant/edit/{restaurant.id}">
                <label class="form-label">Restaurant Name:</label>
                <input 
                    name="name"
                    class="form-control" 
                    value="{restaurant.name}"
                >
                <div class="text-center">
                    <button class="btn btn-primary mt-4 mx-auto w-50">
                        Edit
                    </button>
                </div>
            </form>
        </div>
    """
    return html