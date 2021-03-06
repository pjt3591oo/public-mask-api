# 약국, 우체국, 농협 등의 마스크 판매처 정보 제공 (마스크 재고 관련 정보는 제공하지 않음)
import requests as rq
import pandas as pd
import urllib, json

BASE_URL = 'https://8oi9s0nnth.apigw.ntruss.com/corona19-masks/v1'
PATH = '/stores/json'
page = 1
perPage = 500 # max: 5000, min: 500, defualt: 500

result = {
  'addr': [],
  'code': [],
  'lat': [],
  'lng': [],
  'name': [],
  'type': [], # 0, 1, 2
}

while True:
  params = {
    'page': page, 
    'perPage': perPage
  }

  res = rq.get(BASE_URL + PATH, params=params)

  json = res.json()
  cnt = json['count']
  stores = json['storeInfos']
  print(page)
  for store in stores:
    addr = store.get('addr', None)
    if addr:
      result['addr'].append(addr)
      result['code'].append(store['code'])
      result['lat'].append(store['lat'])
      result['lng'].append(store['lng'])
      result['name'].append(store['name'])
      result['type'].append(store['type'])
  
  if cnt != 500:
    break

  page += 1

df = pd.DataFrame(result)
df.to_csv('stores_info.csv')
print(page, '페이지 끝.')