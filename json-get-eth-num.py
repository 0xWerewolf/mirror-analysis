import json
import csv

AuctionEndedTopic = "0xc07c8c3aa4357ff71dbb73989298b2b27ad41a7216d9846113d7377a8e5f4158"

with open('./code.json', mode='r') as log_file:
    results = json.loads(log_file.read())['result']

total = 0
for result in results:
    if result['topics'][0]==AuctionEndedTopic:
        beginIdx = 2+64*3
        amountLen = 64
        amountHex = result['data'][beginIdx:beginIdx+amountLen]
        print("amount hex: "+amountHex)
        print("amount int: ")
        amount = int(amountHex, 16)
        print( amount/1000000000000000000 ,"ETH")
        total += amount
        # 写入csv，根据address -> line -> new column "winner price"
        csv.writer()
print("TOTAL:", total)
print("readable:", total/1000000000000000000, "ETH")
# 11840000000000000000
