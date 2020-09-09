import requests
import json

with open("demo1.json", 'r', encoding='utf-8') as f:
    data = json.load(f)
    print(data)

url = data['url']

params = data['params']

method = data['method']

headers = {
    'content-type': 'application/x-www-form-urlencoded'
}

res = requests.request(method=method, url=url, params=params,headers= headers)



print(res.text)

# res_dict = res.json()# 将响应转为json对象（字典）等同于`json.loads(res.text)
#
# print(res_dict["code"])
#
# json_text = json.dumps(res_dict, indent=2, sort_keys=True, ensure_ascii=False)



# url = 'http://openapi.tuling123.com/openapi/api/v2'
#
# data = '''{
#         'name' = 'hanzhichao'
#         'age' = 18
#         }'''
# data = '{"name":"hanzhichao,"age"=18}'
#
# res = requests.post(url=url, data=data)
#
# print(res.text)