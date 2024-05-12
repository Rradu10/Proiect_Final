from flask import Flask, render_template, request, redirect, url_for
from models import Product, Service

app = Flask(__name__)


products = [
    Product(1, 'Laptop', 'Powerful laptop for all your needs', 5299, 'https://s13emagst.akamaized.net/products/46530/46529799/images/res_3b47b1f9f918618aa260a53bfbbb426d.jpg?width=720&height=720&hash=7EF6DA5328022393937847AF4E6842B6'),
    Product(2, 'Smartphone', 'Latest smartphone with amazing features', 3109, 'https://s13emagst.akamaized.net/products/52576/52575496/images/res_a54ef0b7af00459e57e280696ca035c8.jpg?width=720&height=720&hash=B433E3C396A84CC7A9601231370446EB'),
    Product(3, 'Tablet', 'Lightweight and portable tablet', 907, 'https://s13emagst.akamaized.net/products/64438/64437252/images/res_3e6054ef4d6340bf43ac317511b9d972.jpg?width=720&height=720&hash=A9407384336732EA59BEA8731C7CEF0A')
]

services = [
    Service(1, 'Web Design', 'Professional web design service'),
    Service(2, 'Graphic Design', 'Creative graphic design service'),
    Service(3, 'Digital Marketing', 'Effective digital marketing solutions')
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/products')
def product_list():
    return render_template('products.html', products=products)

@app.route('/products/<int:id>')
def product_detail(id):
    product = next((p for p in products if p.id == id), None)
    if product:
        return render_template('product_detail.html', product=product)
    return 'Product not found', 404

@app.route('/services')
def service_list():
    return render_template('services.html', services=services)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':

        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        return redirect(url_for('index'))
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
