#!/bin/bash
key="`cat key.txt`"
url="https://www.alphavantage.co/query"
script="import requests
params = {'function':'TIME_SERIES_MONTHLY','symbol':'MSFT', 'apikey':'$key'}
with requests.get('$url', params=params) as r:
	results = r.json()
	results = list(results['Monthly Time Series'].items())[:3]
	print(results)
"
python -c "$script"