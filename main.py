import bs4
import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest
order = requests.get('https://delta-computer.net/index.php/en/laptop/asus')
sorce = order.content
#print(sorce)
BSoup = bs4.BeautifulSoup(sorce)
#print(BSoup)
lap_name = BSoup.find_all("div",{'class':'vm-product-descr-container vm-product-descr-container-0'})
lap_price = BSoup.find_all("span",{'class':'PricesalesPrice'})
#print(lap_price)
#<div class="vm-product-descr-container vm-product-descr-container-0">
# <span class="PricesalesPrice">43500,00 LE</span>
list_m =[]
for i in range(len(lap_name)):
    list_m.append(lap_name[i].text)

    print(list_m[i].replace('\n','') )