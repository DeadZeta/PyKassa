api_url = "https://www.free-kassa.ru/merchant/cash.php?"
merchant_id = 74510
secret_key = 'uadw2zvh'

products = {
	0: {
		"name": 'Услуга #1',
		"price": 10,
		"command": 'service %name% 1'
	},

	1: {
		"name": 'Услуга #2',
		"price": 15,
		"command": 'service %name% 2'
	},

	2: {
		"name": 'Услуга #3',
		"price": 20,
		"command": 'service %name% 3'
	}
}
