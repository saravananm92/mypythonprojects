#!/usr/bin/python

import sys
from urllib import urlopen as ureq
from bs4 import BeautifulSoup as soup

company_code = sys.argv[1]

my_url = "https://finance.google.com/finance?q=" + str(company_code)

try : 
    uclient = ureq(my_url)
except : 
    print "Offline"
    quit()

finally :
    page_html = uclient.read()
    page_soup = soup(page_html,"html.parser")
    stock_price = page_soup.findAll("span",{"class":"pr"})[0].text
    print stock_price.strip()


