import requests
# r = requests.get('https://api.blockcypher.com/v1/btc/main')
# print(r.json())

# height = r.json()['height']

# r = requests.get('https://api.blockcypher.com/v1/btc/main/blocks/' + str(height) + '?txstart=1&limit=500')

# print(r.json())

# r = requests.get('https://api.blockcypher.com/v1/btc/main/blocks/' + str(height) + '?txstart=500&limit=500')

# print(r.json())

# r = requests.get('https://api.blockcypher.com/v1/btc/main/blocks/' + str(height) + '?txstart=1000&limit=500')

# print(r.json())

# # 89d231aefde5f3c08b633ace6e4b0138222ca99001ca150dbc7d99c5568543cd

# r = requests.get('https://api.blockcypher.com/v1/btc/main/txs/8466c24f2687963d60f8da6b756a396492c9de71cca9dd97d7953a4afd170a83')

# print(r.json())

r = requests.get('https://blockchain.info/rawtx/8466c24f2687963d60f8da6b756a396492c9de71cca9dd97d7953a4afd170a83')

print(r.json())
