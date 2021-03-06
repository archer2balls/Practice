# -*- coding: utf-8 -*-
"""RSI.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1prf2SvYniWiEIBbSCdmiuSJAIpSxkjH2
"""

#Description: Use the Relative Strength Index (RSI) and Python to determine if a stock is being over bought or over sold

# import the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

#Load the data
from google.colab import files
uploaded = files.upload()

#Store the data
GOOG = pd.read_csv('GOOG.csv')
#Show the data
GOOG

#Visualise the data
plt.figure(figsize=(12.5, 4.5))
plt.plot(GOOG['Adj Close'], label = 'GOOG')
plt.title('Google Adj. Close Price History')
plt.xlabel('Nov 25, 2019 - Nov 20, 2020')
plt.ylabel('Adj. Close Price USD ($)')
plt.legend(loc='upper left')
plt.show()

#Create the simple moving average with a 30 day window
SMA30 = pd.DataFrame()
SMA30['Adj Close'] = GOOG['Adj Close'].rolling(window= 30).mean()
SMA30

#Create a simple moving average with a 100 day window
SMA100 = pd.DataFrame()
SMA100['Adj Close'] = GOOG['Adj Close'].rolling(window= 100).mean()
SMA100

#Visualise the data
plt.figure(figsize=(12.5, 4.5))
plt.plot(GOOG['Adj Close'], label = 'GOOG')
plt.plot(SMA30['Adj Close'], label = 'SMA30')
plt.plot(SMA100['Adj Close'], label = 'SMA100')
plt.title('Google Adj. Close Price History')
plt.xlabel('Nov 25, 2019 - Nov 20, 2020')
plt.ylabel('Adj. Close Price USD ($)')
plt.legend(loc='upper left')
plt.show()

#new data frame to store all the data
data = pd.DataFrame()
data['GOOG'] = GOOG['Adj Close']
data['SMA30'] = SMA30['Adj Close']
data['SMA100'] = SMA100['Adj Close']
data

#Create a function to signal when to buy and sell the asset/stock
def buy_sell(data):
  sigPriceBuy = []
  sigPriceSell = []
  flag = -1

  for i in range(len(data)):
    if data['SMA30'][i] > data['SMA100'][i]:
      if flag != 1:
        sigPriceBuy.append(data['GOOG'][i])
        sigPriceSell.append(np.nan)
        flag = 1
      else:
        sigPriceBuy.append(np.nan)
        sigPriceSell.append(np.nan)
    elif data['SMA30'][i] < data['SMA100'][i]:
      if flag != 0:
        sigPriceBuy.append(np.nan)
        sigPriceSell.append(data['GOOG'][i])
        flag = 0
      else:
        sigPriceBuy.append(np.nan)
        sigPriceSell.append(np.nan)
    else:
        sigPriceBuy.append(np.nan)
        sigPriceSell.append(np.nan)

  return (sigPriceBuy, sigPriceSell)

#Store the buy and sell data into a variable
buy_sell = buy_sell(data)
data['Buy_Signal_Price'] = buy_sell[0]
data['Sell_Signal_Price'] = buy_sell[1]

#Show the data
data

#Visulise the data and the strategy to buy and sell the stock
plt.figure(figsize=(12.5, 4.5))
plt.plot(data['GOOG'], label = 'GOOG', alpha = 0.35)
plt.plot(data['SMA30'], label = 'SMA30', alpha = 0.35)
plt.plot(data['SMA100'], label = 'SMA100', alpha = 0.35)
plt.scatter(data.index, data['Buy_Signal_Price'], label = 'Buy', marker = '^', color = 'green', alpha = 1)
plt.scatter(data.index, data['Sell_Signal_Price'], label = 'Sell', marker = 'v', color = 'red', alpha = 1)
plt.title('Google Adj. Close Price History Buy & Sell Signals')
plt.xlabel('Nov 25, 2019 - Nov 20, 2020')
plt.ylabel('Adj. Close Price USD ($)')
plt.legend(loc='upper left')
plt.show()