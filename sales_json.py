# 약국, 우체국, 농협 등의 마스크 판매처 정보 제공 (마스크 재고 관련 정보는 제공하지 않음)
import requests as rq
import pandas as pd
import urllib, json

BASE_URL = 'https://8oi9s0nnth.apigw.ntruss.com/corona19-masks/v1'
PATH = '/sales/json'
page = 1
perPage = 500 # max: 5000, min: 500, defualt: 500

result = {
  'code': [],
  'stock_at': [],
  'remain_stat': [],
  'created_at': [],
}

while True:
  params = {
    'page': page, 
    'perPage': perPage
  }

  res = rq.get(BASE_URL + PATH, params=params)

  json = res.json()
  cnt = json['count']
  stores = json['sales']
  print(page)
  for store in stores:
    stock_at = store.get('stock_at', None)
    if stock_at:
      result['code'].append(store['code'])
      result['stock_at'].append(store['stock_at'])
      result['remain_stat'].append(store['remain_stat'])
      result['created_at'].append(store['created_at'])

  
  if cnt != perPage:
    break

  page += 1

df = pd.DataFrame(result)
df.to_csv('sales_info.csv')
print(page, '페이지 끝.')