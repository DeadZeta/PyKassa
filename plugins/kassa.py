from config import merchant_id, secret_key, api_url
from time import time
from urllib.parse import urlencode
from hashlib import md5

def generate_sign(params):
    """ Функция для создание цифровой подписи (нужно для кассы) """

    sign = [str(merchant_id), str(params['price']), str(secret_key), str(int(time()))]
    sign = ":".join(sign)
    sign = md5(sign.encode('utf-8'))

    params = {'m': merchant_id, 'oa': params['price'], 'o': int(time()), 'sign': sign.hexdigest(), 'us_username': params['username'], 'us_product': params['product']}
    return params

def generate_url(username='', price=0, product=[]):
    """ Функция для генерации URL для оплаты """
    if username == '' or price == 0 or product == []:
        return "Error: username or sum not filled"

    query = generate_sign({'username': username, 'price': price, 'product': product[0]})
    return api_url + urlencode(query)