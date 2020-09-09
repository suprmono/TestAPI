import requests
import json

with open("demo2.json", 'r', encoding='utf-8') as f:
    data_dict = json.load(f)
    print(data_dict)

url = data_dict['url']

# params = data_dict['params']

method = data_dict['method']

headers = {
    'content-type': 'application/json'
}

data = data_dict['data']

res = requests.request(method=method, url=url, headers=headers, json=data)

print(json.dumps(json.loads(res.text), indent=2, sort_keys=True, ensure_ascii=False))