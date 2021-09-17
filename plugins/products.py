from config import products
from json import dumps

def generate_html_option():
	""" Функция для сборки html-опций из Продуктов """

	options = ""

	for item in products.items():
		options += f"<option value=\"" + str(item[0]) + "\">" + item[1]['name'] + " -> " + str(item[1]['price']) + "</option>\n"

	return options

def get_product(product_id):
	""" Функция для получения продукта по id """

	return list(products.items())[int(product_id)][1]

def json_get_product(product_id):
	""" Функция для получения продукта по id в виде JSON"""
	return dumps(get_product(product_id))
