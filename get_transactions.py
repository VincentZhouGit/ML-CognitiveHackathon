import requests
import json
import sys

addresses = sys.argv[1:len(sys.argv)]

transaction_data = {}
for address in addresses:
	request='http://api.etherscan.io/api?module=account&action=txlist&address=' + address + '&startblock=0&endblock=99999999&sort=asc&apikey=RZAZS4BMIJ4M6Z1N38UAVDY32KW1H79NQR'
	response = requests.get(request)
	print(response)
	content = json.loads(response.content)
	transactions =  content['result']
	for tx in transactions:
		# ignore contract creations and internal transactions
		if len(tx['input']) is 2:
			transaction_data[tx['hash']] = {'from': tx['from'],'to': tx['to'],'value': tx['value']}

with open ('dat/transactions.json', 'w') as outfile:
	json.dump(transaction_data, outfile)

