import requests

url = 'https://api.exchangerate-api.com/v6/latest'

req = requests.get(url)
resp =  req.status_code

if resp == 200:
  print('ok')
else:
  print('Nao encontrado!')