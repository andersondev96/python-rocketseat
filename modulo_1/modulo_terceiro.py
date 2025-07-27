# pip3 install requests==2.31.0

print("Importação e uso de módulo de terceiros")
import requests

url = "https://www.example.com"
response = requests.get(url)
print(f"Solicitação HTTP para {url} retornou o status {response.status_code}")