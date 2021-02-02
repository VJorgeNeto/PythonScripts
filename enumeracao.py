import requests
import json

for i in range(4):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/'+ str(i)) #enumeração de pagina convertendo i(int) em str
    json_text = response.status_code #trazendo status da pagina para cada combinação
    print(json_text)
