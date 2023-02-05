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

app = FastAPI()


def database_connection():
    connect(db="stock",
            host="127.0.0.1",
            port=27017)


database_connection()


def scraping_machine():

    def writeData():
        stock_prices = StockPrices()
        stock_prices.stock_name = "Animesh"
        stock_prices.stock_last_trade_price = "Animesh"
        stock_prices.stock_high_price = "Animesh"
        stock_prices.low_price = "Animesh"
        stock_prices.stock_close_price = "Animesh"
        stock_prices.stock_previous_close = "Animesh"
        stock_prices.percent_change = "Animesh"
        stock_prices.trade_number = "Animesh"
        stock_prices.value = "Animesh"
        stock_prices.stock_volume = "Animesh"
        stock_prices.save()
    
    
    def send_database(soup):
        all = soup.find_all(class_="table-responsive")
        new_all = all[0].find_all("tr")
        all_items = StockPrices.objects
        if date.today().day == 1:
            all_items.drop_collection()
            for i in range(1, len(new_all)):
                one_tr = new_all[i]
                stock_prices = StockPrices()
                stock_prices.stock_name = one_tr.find_all("td")[1].text.replace("\t", "").replace("\n", "")
                stock_prices.stock_last_trade_price = one_tr.find_all("td")[2].text
                stock_prices.stock_high_price = one_tr.find_all("td")[3].text
                stock_prices.low_price = one_tr.find_all("td")[4].text
                stock_prices.stock_close_price = one_tr.find_all("td")[5].text
                stock_prices.stock_previous_close = one_tr.find_all("td")[6].text
                stock_prices.percent_change = one_tr.find_all("td")[7].text
                stock_prices.trade_number = one_tr.find_all("td")[8].text
                stock_prices.value = one_tr.find_all("td")[9].text
                stock_prices.stock_volume = one_tr.find_all("td")[10].text
                stock_prices.save()
        else:
            for i in range(1, len(new_all)):
                one_tr = new_all[i]
                all_items[i - 1].update(stock_name=one_tr.find_all("td")[1].text.replace("\t", "").replace("\n", ""),
                                        stock_last_trade_price=one_tr.find_all("td")[2].text,
                                        stock_high_price=one_tr.find_all("td")[3].text,
                                        stock_low_price=one_tr.find_all("td")[4].text,
                                        stock_close_price=one_tr.find_all("td")[5].text,
                                        stock_previous_close=one_tr.find_all("td")[6].text,
                                        percent_change=one_tr.find_all("td")[7].text,
                                        trade_number=one_tr.find_all("td")[8].text,
                                        value=one_tr.find_all("td")[9].text,
                                        stock_volume=one_tr.find_all("td")[10].text)

    def keep_scraping():
        # page = requests.get("https://www.dsebd.org/latest_share_price_scroll_l.php")
        # soup = BeautifulSoup(page.content, 'html5lib')
        # print(soup)
        writeData()
        # send_database(soup)

    day_name = datetime.datetime.now().strftime("%w")
    hour = datetime.datetime.now().strftime("%H")
    if day_name == 5 or day_name == 6:
        pass
    else:
        keep_scraping()
        print("Scraping Working")
        # if 10 < int(hour) < 15:
        #     keep_scraping()
        # elif int(hour) == 16:
        #     pass
        # else:
        #     print("Market closed")


@app.get("/stockprices")
def get_stock_prices():
    stock_info_list = []
    for i in StockPrices.objects:
        stock_info_list.append({
            "stock_name": i.stock_name,
            "price": i.stock_last_trade_price
        })
    return stock_info_list

def run_scraping_machine():
    while True:
        scraping_machine()
        time.sleep(20)


t1 = threading.Thread(target=run_scraping_machine)
t1.start()
