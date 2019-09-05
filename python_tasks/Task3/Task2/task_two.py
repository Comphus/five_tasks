import requests

#opening the file that contains the API key
with open("key.txt") as k:
	key = k.read()

params = {"function":"TIME_SERIES_MONTHLY","symbol":"MSFT", "apikey":key}
def get_monthly(URL, params):
	with requests.get("https://www.alphavantage.co/query", params=params) as r:
		results = r.json()
		results = list(results["Monthly Time Series"].items())[:3]
		return results

if __name__ == "__main__":
	print(get_monthly("https://www.alphavantage.co/query",params))