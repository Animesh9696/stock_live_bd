from typing import Union
from fastapi import FastAPI
import time
from mongoengine import connect
import datetime
import requests
import threading
from bs4 import BeautifulSoup
from schema.schema import *
from datetime import date


page = requests.get("https://www.dsebd.org/latest_share_price_scroll_l.php")
soup = BeautifulSoup(page.content, 'html5lib')

all = soup.find_all(class_="table-responsive")
new_all = all[0].find_all("tr")
# all_items = StockPrices.objects
# print(new_all[1].find_all("td")[1].text.strip())
print(new_all[1].find_all("td")[2].text.strip())