import flask

# Set up the Flask app
app = flask.Flask(__name__)

# Set up a list of products
products = [
    {
        "id": 1,
        "name": "Photography Package",
        "description": "A package of professional photography services for events and portraits.",
        "price": 500.00
    },
    {
        "id": 2,
        "name": "Video Editing Package",
        "description": "A package of professional video editing services for events, promotional videos, and more.",
        "price": 750.00
    },
    {
        "id": 3,
        "name": "T-Shirt Delivery",
        "description": "Delivery of a custom T-shirt to your location.",
        "price": 25.00
    }
]

# Set up a cart for the user's purchases
cart = []

# Define a route to display the homepage
@app.route("/")
def index():
    return flask.render_template("index.html", products=products)

# Define a route to display the product page
@app.route("/product/<int:product_id>")
def product(product_id):
    # Find the product with the given ID
    product = next(p for p in products if p["id"] == product_id)

    # Render the product page template
    return flask.render_template("product.html", product=product)

# Define a route to add a product to the cart
@app.route("/add_to_cart/<int:product_id>")
def add_to_cart(product_id):
    # Find the product with the given ID
    product = next(p for p in products if p["id"] == product_id)

    # Add the product to the cart
    cart.append(product)

    # Redirect the user back to the homepage
    return flask.redirect("/")

# Define a route to display the cart
@app.route("/cart")
def show_cart():
    # Render the cart template
    return flask.render_template("cart.html", cart=cart)

# Define a route to checkout and place the order
@app.route("/checkout")
def checkout():
    # Calculate the total cost of the order
    total_cost = sum(p["price"] for p in cart)

    # Clear the cart
    cart.clear()

    # Render the checkout template
    return flask.render_template("checkout.html", total_cost=total_cost)

# Run the app
if __name__ == "__main__":
    app.run()
