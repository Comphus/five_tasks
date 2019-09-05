#!/bin/bash
key="`cat key.txt`"
url="https://www.alphavantage.co/query"
echo $key
res=$(curl -X POST -H "Content-Type: application/json" \
--data '{ "function":"TIME_SERIES_MONTHLY","symbol":"MSFT", "apikey":"$key" }' \
$url\
exit 0)

echo $res