import requests as rq
import pandas as pd
import geocoder

url = 'https://8oi9s0nnth.apigw.ntruss.com/corona19-masks/v1/storesByAddr/json'

params={
  'address': '경기도 파주시 파주읍'
}
res = rq.get(url, params=params)
json = res.json()
m = 10000

stores = json['stores']
count = json['count']

data = {
  "addr": [],
  "created_at": [],
  "name": [],
  "store_type": [],
  "remain_stat": [],
}

'''
few: 조금
some: 약간
plenty: 많은
'''

for store in stores:
  addr = store['addr']
  created_at = store['created_at']
  name = store['name']
  store_type = store['type']
  remain_stat = store.get('remain_stat', '')
  data['addr'].append(addr)
  data['created_at'].append(created_at)
  data['name'].append(name)
  data['store_type'].append(store_type)
  data['remain_stat'].append(remain_stat)
  print('addr: %s, created_at: %s, name: %s, store_type: %s, remain_stat: %s'%(addr, created_at, name, store_type, remain_stat))


df = pd.DataFrame(data)
df.to_csv('storesByAddr_json.csv')