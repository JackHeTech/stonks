import requests
import json 
import time 
from dotenv import load_dotenv
import os
load_dotenv()


print("what is the stock symbol?") 
stock_symbol = str(input()) # GME

print("how long do you want to monitor " + stock_symbol + " while you do other stuff? (in hours)") 
end_time_input = int(input()) 
end_time = end_time_input * 3600 

print("who often do I fetch data? (in seconds)")
interval_time_input = int(input()) # in seconds 
interval_time = interval_time_input  

print("What is your target price?")
target_price = int(input()) # in USD

print("What is your lower bound price?")
lower_bound = int(input()) # in USD


print("OK, I will monitor " + stock_symbol + " price for " + str(end_time_input) + " hours every " + str(interval_time_input) + " seconds.")

url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-holders"

querystring = {"symbol":stock_symbol,"region":"US"}

SECRET_KEY = os.getenv("API_KEY")
API_HOST = os.getenv("HOST")

headers = {
    'x-rapidapi-key': SECRET_KEY,
    'x-rapidapi-host': API_HOST
}

time_elapsed = 0
print("ending in: " + str(end_time) + " seconds.")
while time_elapsed <= end_time:
    response = requests.request("GET", url, headers=headers, params=querystring)
    data = json.loads(response.text) 
    market_price = int(data['price']['regularMarketPrice']['raw'])
    print("currency: " + str(data['price']['currency']))
    print("premarket price: " + str(data['price']['preMarketPrice'])) 
    print("postmarket price: " + str(data['price']['postMarketPrice'])) 
    print("current market price: " + str(market_price)) 

    if market_price >= target_price: 
        # price hits target!
        os.system("afplay /Users/jackhe/Developer/gme/money.mp3")
    elif market_price <= lower_bound: 
        # shit. 
        os.system("afplay /Users/jackhe/Developer/gme/guh.mp3")

    time_elapsed += interval_time 
    time.sleep(interval_time)
    print(time_elapsed)
    print("===================================================================") 