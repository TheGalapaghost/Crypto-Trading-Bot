import pandas as pd
import cbpro
import hmac, hashlib, time, requests, os
from requests.auth import AuthBase
import matplotlib.pyplot as plt
from mpl_finance import candlestick_ohlc
import pandas as pd
import matplotlib.dates as mpl_dates
import datetime
from datetime import datetime
from pytz import timezone
from auth_credentials import (api_secret, api_pass, api_key, sand_api_secret, sand_api_pass, sand_api_key)
from Math_RSI import Math_RSI
from Math_MACD import Math_MACD
from Stochastic_oscillator import stochastic
import math

pair = "BTC-USD"
splitter = pair.split('-')
tender = splitter[1]
coin = splitter[0]
candle_time = 2

data_tracker = 0

            
sand_url = "https://api-public.sandbox.pro.coinbase.com"
url = 'https://api.pro.coinbase.com/'
client = cbpro.AuthenticatedClient(sand_api_key, sand_api_secret, sand_api_pass, api_url=sand_url)
#client = cbpro.AuthenticatedClient(api_key,api_secret,api_pass, api_url=url)

def get_crypto_balance(crypto_ticker):
    x = client.get_accounts()
    for accounts in x:
        for indies in accounts.values():
            if indies == crypto_ticker:
                return list(accounts.values())[2]

def buy(tender):
    full = math.floor(float(get_crypto_balance(tender)))
    client.place_market_order(product_id=pair, side='buy', funds=full)
def sell(coin):
    full_crypto = float(get_crypto_balance(coin))
    full_crypto = round(full_crypto, 8)
    client.place_market_order(product_id=pair, side='sell', size=full_crypto)


prices_RSI = []
prices_MACD = []
close_stochastic = []
prices_stochastic = []
stochastic_lows = []
stochastic_highs = []

RSI = []
MACD = []
stoch_list = []

botmeter = 0
start = 0

header = ["Time(s)", "Open", "High", "Low", "Close"]

time_count = 0

f = time.time()

rsi_ch = -3

while True:
    if start == 0:
      print("\nData Initiation Has Begun!\n")
      print("\nLogged Data Points: " + str(data_tracker))
      print("\nRemaining Data Points: " + str((26+8)-data_tracker))
      print("\nEstimated Initiation Time: " + str((((26+8)-data_tracker)*candle_time)/60) + " minutes")
      start = 1
    time.sleep(1)
    a = client.get_product_ticker(pair)
    price_val = float(a['price'])
    prices_stochastic.append(price_val)
    
    
    
    
    z = time.time()
    
    if ((z-f)>candle_time):
        prices_RSI.append(prices_stochastic[-1])
        prices_MACD.append(prices_stochastic[-1])
        close_stochastic.append(prices_stochastic[-1])
        stochastic_lows.append(min(prices_stochastic))
        stochastic_highs.append(max(prices_stochastic))

        stochastic_prices = []
        #print(prices_MACD)
        f = time.time()
        if len(prices_RSI) > 14:
            rsi = Math_RSI(prices_RSI)
            
        if len(close_stochastic) > 20:
            stoch = stochastic(stochastic_highs, stochastic_lows, close_stochastic)
            stoch_list.append(stoch)
            
        
        if len(prices_MACD) > 26+8:
            macd = Math_MACD(prices_MACD)
        try:
            print("\nMACD: ", macd[-1])
            print("\nRSI: ", rsi[-1])
            print("\nStochastic: ", stoch)
            
            #if rsi < 30 and macd[-1] == 1:
               #print("Confident Buy")
            
            botmeter+=stoch
        
            if rsi[-1] < 30:
                botmeter+=3
                #print("Semi-Confident Buy {RSI in favor, MACD is not}")
        
            if macd[-1] == 1:
                reader = []
                botmeter+=9
                for i,x in zip(rsi[rsi_ch:], stoch_list[rsi_ch:]):
                    #print(i)
                    #print(x)
                    if i < 30 and x == 4:
                        reader.append(1)
                        #botmeter+=35
                        #break   
                    elif i < 30 and x != 4:
                        reader.append(2)
                        #botmeter+=15
                        #break
                    elif i > 30 and x == 4:
                        reader.append(2)
                        #botmeter+=15
                        #break
                    else:
                        reader.append(0)
                        
                if 1 in reader:
                    botmeter+=35
                elif 2 in reader:
                    botmeter+=15
                else:
                    pass
                        
                        
            
                #print("Semi-Confident Buy {MACD in favor, RSI is not}")
        
            #if rsi[-1] > 70 and macd[-1] == -1:
                #print("Confident Sell")
        
            if rsi[-1] > 70:
                botmeter-=3
                #print("Semi-Confident Sell {RSI in favor, MACD is not}")
        
            if macd[-1] == -1:
                reader = []
                botmeter-=9
                for i,x in zip(rsi[rsi_ch:], stoch_list[rsi_ch:]):
                    if i > 70 and x == -4:
                        reader.append(-1)
                        #botmeter-=35
                        #break
                    elif i > 70 and x != -4:
                        reader.append(-2)
                        #botmeter-=15
                        #break
                    elif i < 70 and x == -4:
                        reader.append(-2)
                        #botmeter-=15
                        #break
                    else:
                        reader.append(0)
                if -1 in reader:
                    botmeter-=35
                elif -2 in reader:
                    botmeter-=15
                else:
                    pass
                    
            if botmeter > 100:
                print("{UPDATE} ==> Bot has been indicated to BUY")
                #command to buy
                #buy(tender)
                botmeter = 0
                
            if botmeter < -100:
                print("{UPDATE} ==> Bot has been indicated to SELL")
                #command to sell
                #sell(coin)
                botmeter = 0
                #print("Semi-Confident Sell {MACD in favor, RSI is not}")
                
            print(botmeter)
        except Exception as e:
            print("ERROR_CHECK: " + str(e))
            if data_tracker == 0:
                print("\nData Initiation Has Begun!\n")
            data_tracker+=1
            print("\nLogged Data Points: " + str(data_tracker))
            print("\nRemaining Data Points: " + str((26+8)-data_tracker))
            print("\nEstimated Initiation Time: " + str((((26+8)-data_tracker)*candle_time)/60) + " minutes")
            pass
        
    
    
    
        

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    