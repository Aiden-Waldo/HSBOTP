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

response = requests.get('https://hypixel.net/skyblock/bazaar')