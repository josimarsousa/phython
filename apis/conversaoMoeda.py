import requests

url = 'https://api.exchangerate-api.com/v6/latest'

req = requests.get(url)
resp =  req.status_code
dados = req.json()

if resp == 200:
  print('Dados encontrados: \n', dados, '\n')
else:
  print('Nao encontrado!')

valor_reais = float(input('Informe o valor em R$ a ser convertido:\n'))
cotacao = dados['rates']['BRL']
print(f'R${valor_reais} em dolar valem US$ {(valor_reais / cotacao):.2f}')

