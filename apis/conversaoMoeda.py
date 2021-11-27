import requests

url = 'https://api.exchangerate-api.com/v6/latest'

req = requests.get(url)
resposta =  req.status_code
if resposta == 200:
  print('ok')
else:
  print('Nao encontrado!')