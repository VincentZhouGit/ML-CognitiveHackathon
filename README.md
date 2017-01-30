## Deloitte Machine Learning Hackathon

Etherscan lists the latest 200,000 accounts at https://etherscan.io/accounts/n, for n from 1 to 8000.

To get all listed accounts from pages n to m, run `./scrape_accounts n m`. This will append the accounts to the file `dat/accounts`.

We then need to get all the transaction for each of the accounts listed. The python script `get_transactions.py` takes in a set
of address and outputs to `dat/transactions.json` a json object of simple value transactions with keys the txhash and values the 
from, to, and value fields of the transaction. Example:

```
$ python get_transactions.py 0xe853c56864a2ebe4576a807d26fdc4a0ada51919 0x7aa534c9b18d6f4117301971962986467e74eed1
```

To manipulate the data from python, use json.load:

```python
>>> import json
>>> with open('dat/transactions.json') as datfile:
>>>	transactions = json.load(datfile)
>>> for txhash in transactions:
>>>	print transactions[txhash]
{u'to': u'0x7aa534c9b18d6f4117301971962986467e74eed1', u'from': u'0x60e16961ad6138d2fb3e556fc284d9c2fff41486', u'value': u'45000000000000000000000'}
{u'to': u'0x7aa534c9b18d6f4117301971962986467e74eed1', u'from': u'0x2a65aca4d5fc5b5c859090a6c34d164135398226', u'value': u'1091361460000000000'}
{u'to': u'0x7aa534c9b18d6f4117301971962986467e74eed1', u'from': u'0x2a65aca4d5fc5b5c859090a6c34d164135398226', u'value': u'1067806950000000000'}
...
```

### TODO

* Apply k-means algorithm to transactions with features: value, gas, gasPrice
* Import JSON transactions into graph analytics
* Prepare presentation
	* Motivation from forensics in Bitcoin
	* Ethereum and blockchain
	* Data scraping
	* Model
	* Feature selection
	* Results
	* Further work
