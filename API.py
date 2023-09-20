# API.py
'''
Talking to Hypixel API
created: 2023-09-02
'''

# changing from ah to bz

'''
legacy

# step 1: establish API connection

import requests

response = requests.get('https://api.hypixel.net/skyblock/auctions')

print(response) # 200 means it works

# step 2: make into list, filter into 'Buy It Now' auctions, and 

# min_bid = int(input("minimum item price: "))
# max_bid = int(input("maximum item price: "))
min_bid = 1000000
max_bid = 200000000

enchants = ['', ]

import json

response = json.loads(json.dumps(response.json(), sort_keys=True, indent=4))
response = response['auctions']
print(len(response))
# print(type(response[0]['starting_bid']))


for i in range(len(response)-1, -1, -1):
    if response[i]['bin'] != True:
        del(response[i])
        continue
    if not min_bid < response[i]['starting_bid'] < max_bid:
        del(response[i])
        continue

print(len(response))
'''

# Step I: get data from API

import requests
import json
# key = '863aa4eb-485c-4c0c-ac39-08e7976f1296'
response = requests.get('https://api.hypixel.net/skyblock/bazaar')
response = json.loads(json.dumps(response.json(), sort_keys=True, indent=4))

products = response['products']


class Product:

    def __str__(self):
        return self.name

    def __init__(self, name, sell_price, buy_price, moving):
        self.name = name
        self.sell_price = int(round(sell_price, 0))
        self.buy_price = int(round(buy_price, 0))
        self.spread = int(round(self.buy_price - self.sell_price, 0))
        self.moving = moving
    
    def stats(self):
        return f"Item: {self.name}\nSell Price: {self.sell_price}\nBuy Price: {self.buy_price}\nSpread: {self.spread}\nWeekly Moving: {self.moving}"
    
things = []

for product in products:
    status = products[product]['quick_status']
    things.append(Product(product, status['sellPrice'], status['buyPrice'], status['sellMovingWeek'] + status['buyMovingWeek']))

things.sort(key=lambda x:x.spread, reverse=True)

for i in range(200, 206):
    print(things[i].stats())
