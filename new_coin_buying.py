from binance.client import Client
from binance import *
import datetime
import time
import pytz
import pandas as pd
import websocket, json


client_secret = {}
client_api = {}

client = client_secret + client_api



#create variable to store the date and time, down to the seconds of current day
now = datetime.datetime


#create variable to store date and time of the day of listing
d_day = datetime.datetime()

#conditional statement that will initiate buy order
if now ==  d_day:
    buy_order = client.order_market_buy(
            symbol = {}, 
            quantity = {})

#create variable to store the current time in seconds
#s1 = time.time()

#creating the websocket
cc = 'ETHUSDT'
interval = '1m'

socket = f'wss://stream.binance.com:9443/ws/{cc}@kline_{interval}'


def on_message(ws, message):
    json_message = json.loads(message)
    high = json_message['k']
    print(float(high))


def on_close(ws):
    print("Connection Closed")



ws = websocket.WebSocketApp(socket, on_message = on_message, on_close = on_close)

ws.run_forever()

#create buy order
buy_order = client.order_market_buy(
    symbol={},
    quantity={})


#create trailing stop or sell order when trailing stop is hit
if on_message <= 0.02 * on_message:
    sell_order = client.order_market_sell(
    symbol={},
    quantity={})








