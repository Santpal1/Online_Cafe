from flask import Flask, render_template, session, redirect, url_for, request

app = Flask(__name__)               # Will create a Flask web application instance

app.secret_key = 'santpal0' 

@app.route('/')
def index():
    if 'cart' not in session:
        session['cart'] = {}
    return render_template('index.html')

@app.route('/')                     # Defining a route for the root URL ('/')
def indexo():                        # that will render the 'index.html' template.
    return render_template('index.html')

@app.route('/menu')                 # Defining a route for the URL ('/menu')
def menu():                         # that will render the 'menu.html' template.
    return render_template('menu.html')

@app.route('/french_vanilla')
def french_vanilla():
    return render_template('french_vanilla.html')

@app.route('/hazelnut')
def hazelnut():
    return render_template('hazelnut.html')

@app.route('/mocha')
def mocha():
    return render_template('mocha.html')

@app.route('/donut')
def donut():
    return render_template('donut.html')

@app.route('/cherry')
def cherry():
    return render_template('cherry.html')

@app.route('/cinnamon')
def cinnamon():
    return render_template('cinnamon.html')

# Route to add items to the cart
@app.route('/add_to_cart/<item>')
def add_to_cart(item):
    cart = session['cart']
    cart[item] = cart.get(item, 0) + 1
    session['cart'] = cart
    return redirect(url_for('view_cart'))

@app.route('/remove_from_cart/<item>', methods=['GET', 'POST'])
def remove_from_cart(item):
    if request.method == 'POST':
        cart = session.get('cart', {})
        
        if item in cart:
            del cart[item]  # Removing the item from the cart
            
        session['cart'] = cart
        return redirect(url_for('view_cart'))

    # In case of a GET request, redirecting to the cart view without performing any removal
    return redirect(url_for('view_cart'))

# Route to view the cart
@app.route('/view_cart')
def view_cart():
    cart = session.get('cart', {})
    return render_template('cart.html', cart=cart)

if __name__ == '__main__':
    # Running the Flask app in debug mode, which provides helpful debugging information.
    app.run(debug=True)