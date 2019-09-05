"""
Second Python Task. Calls the alphavantage API
The call will request the monthly time series for Microsoft. 
Then the function will return the first three monthly results

Written by Gabriel Lopez
"""
import requests

#opening the file that contains the API key. Reads a file for security purposes
with open("key.txt") as k:
	key = k.read()

params = {"function":"TIME_SERIES_MONTHLY","symbol":"MSFT", "apikey":key}
def get_monthly(URL, params):
	"""
	The main function used to complete Task #2
	Calls the alphavantage API, requesting 'Monthly Time Series'
	Then takes the first three JSON results once the API responds

	Args:
		URL: The alphavantage website URL
		params: The additional parameters for the API request
	"""
	with requests.get("https://www.alphavantage.co/query", params=params) as r:
		results = r.json()
		results = list(results["Monthly Time Series"].items())[:3]
		return results

if __name__ == "__main__":
	print(get_monthly("https://www.alphavantage.co/query",params))