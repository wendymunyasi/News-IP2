import requests

# res = requests.get('https://newsapi.org/v2/sources?apiKey=8d6348db261b49e5b9ad6fc22f7e48f6')

# if res:
#     print('Response ok')
# else:
#     print('Response fail')

# print(res.json)

url = 'https://newsapi.org/v2/sources?apiKey=8d6348db261b49e5b9ad6fc22f7e48f6'

res = requests.get(url)

