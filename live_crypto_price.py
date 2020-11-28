# -*- coding: utf-8 -*-
"""Live Crypto Price.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zK1KboZWEqGZdDchPqjEmtMLdNt-nJac
"""

#Description: This program gets the price of cryptocurrencies in realtime

#Import the libraries
from bs4 import BeautifulSoup
import requests
import time

#Get the URL
#     https://www.google.co.uk/search?q=litecoin+price
#     https://www.google.com/search?q=litecoin+price
url = 'https://www.google.com/search?q=bitcoin+price'

#Make a request to the website
HTML = requests.get(url)

#Parse the HTML
soup = BeautifulSoup(HTML.text, 'html.parser')

#Print soup to find where the text is that contains the price of the cryptocurrency
print(soup.prettify())

# <div class="BNeawe iBp4i AP7Wnd">

#Create a function to get the price of a cryptocurrency
def get_crypto_price(coin):
  #Get the URL
  #      https://www.google.com/search?q=litecoin+price
  url = 'https://www.google.com/search?q='+coin+'+price'

  #Make a request to the website
  HTML = requests.get(url)

  #Parse the HTML
  soup = BeautifulSoup(HTML.text, 'html.parser')

  #Find the current price
  text = soup.find('div', attrs={'class':'BNeawe iBp4i AP7Wnd'}).find('div', attrs={'class':'BNeawe iBp4i AP7Wnd'}).text

  #Return the text
  return text

#Get the price of a crypto currency
price = get_crypto_price('litecoin')

#Print the price
print(price)

#Create a function to consistently show the price of the cryptocureency when it changes
def main():
  last_price = -1
  #Create a loop to continuosly show the price
  while True:
    #Choose the crypto currency that I want ot get the for
    crypto = 'litecoin'
    #Get the price of the cryptocurrency
    price=get_crypto_price(crypto)
    #Check if the price has changed
    if price !=last_price:
      print(crypto+' price: ', price)
      last_price = price
    time.sleep(3)

#Run/execute the main function
main()