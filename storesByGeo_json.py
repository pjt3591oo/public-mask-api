import requests as rq
import pandas as pd
import geocoder

def get_masks(lat, lng, m=3000):
  url = 'https://8oi9s0nnth.apigw.ntruss.com/corona19-masks/v1/storesByGeo/json'

  params = {'lat': lat, 'lng': lng, 'm': m}

  res = rq.get(url, params=params)
  return res.json()

lat = 37.830743
lng = 126.819744
m = 10000

masks = get_masks(lat, lng, m)
stores = masks['stores']
count = masks['count']

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
df.to_csv('storesByGeo_json.csv')