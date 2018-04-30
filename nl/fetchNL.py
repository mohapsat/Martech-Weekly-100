# Packages
# --Web scraping packages

# pip3 install beautifulsoup4
from bs4 import BeautifulSoup as bs
import html5lib
import requests
# import pandas as pd
# import numpy as np

BASE_URI = 'http://martech101.com/?q=&hPP=2&idx=idx_mt101&p=0'

html = requests.get(BASE_URI).text
# print(html)

# pip3 install html5lib
soup = bs(html, 'html5lib')

# print(soup.prettify())

for i in soup.find('div',{"class":"hits"}):
    print(i)
