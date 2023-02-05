from mongoengine import Document, StringField, EmailField

class StockPrices(Document):
    stock_name = StringField(max_length=50)
    stock_open_price = StringField(max_length=50)
    stock_last_trade_price = StringField(max_length=50)
    stock_close_price = StringField(max_length=50)
    stock_previous_close = StringField(max_length=50)
    stock_volume = StringField(max_length=50)
    stock_number_of_trades = StringField(max_length=50)
    stock_high_price = StringField(max_length=50)
    stock_low_price = StringField(max_length=50)
    trade_number = StringField(max_length=50)
    percent_change = StringField(max_length=50)
    value = StringField(max_length=50)
