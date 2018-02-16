#!/usr/bin/python

from urllib import urlopen as ureq
import json
import sys

currency = sys.argv[1]

#crypto currency API url
my_url = "https://api.coinmarketcap.com/v1/ticker/" + str(currency) + "/?convert=INR"

try:
    uclient = ureq(my_url)
except Exception as e:
    print "Offline"
    quit()
finally:
    response = uclient.read()
    result_set = json.loads(response)
    crypto_price_inr = result_set[0]["price_inr"]
    print crypto_price_inr
