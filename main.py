#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
from flask import Flask, request, redirect, url_for, render_template
from markupsafe import Markup
from requests import get
from json import dumps
import os
import plugins.kassa
import plugins.products

TEMPLATE_DIR = os.path.abspath('templates')
STATIC_DIR = os.path.abspath('static')

app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)

@app.route('/')
def index():
    option = plugins.products.generate_html_option()
    return render_template('index.html', option=Markup(option))

@app.route('/api/product/get', methods=['POST'])
def product_get():
    """ Функция для AJAX-запроса на получние информации о продукте """

    if request.method == "POST" and len(request.form) > 0:
        return plugins.products.json_get_product(request.form['id'])

    return "{\"error\": 0}"

@app.route('/api/kassa/generate', methods=['POST'])
def kassa_generate():
    """ Функция для AJAX-запроса на получние ссылки для оплаты продукта """
    if request.method == "POST" and len(request.form) > 0:
        username = request.form['username']
        product = request.form['product']
        product = plugins.products.get_product(product)

        return dumps({"url": plugins.kassa.generate_url(username, product['price'], [request.form['product'], product])})

    return redirect(url_for('index'), code=302)

if __name__ == "__main__":
    app.run(debug=True)
