import requests
from bs4 import BeautifulSoup
import json

url = "https://miuniversoverde.com/vida-cotidiana/aditivos-alimentiarios-numeros-e/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

tablas = soup.find_all('table')

aditivos = []

for tabla in tablas:
    filas = tabla.find_all('tr')

    for fila in filas:
        cols = fila.find_all('td')
        if len(cols) >= 4:
            aditivo = {}
            aditivo['Numero'] = cols[0].text.strip()
            aditivo['Enlace_Numero'] = cols[0].find('a')['href'] if cols[0].find('a') else None
            aditivo['Clasificacion_Vegana'] = cols[1].text.strip()

            if cols[2].find('a'):
                aditivo['Nombre'] = cols[2].find('a').text.strip()
                aditivo['Enlace_Nombre'] = cols[2].find('a')['href']
            else:
                aditivo['Nombre'] = cols[2].text.strip()
                aditivo['Enlace_Nombre'] = None
            
            aditivo['Definicion'] = cols[3].text.strip()
            aditivos.append(aditivo)

with open('../data/aditivosV2.json', 'w', encoding='utf-8') as file:
    json.dump(aditivos, file, ensure_ascii=False, indent=4)

print(response.status_code)  # Debe ser 200
if response.status_code != 200:
    print("Error al cargar la página")
print("Datos extraidos y guardados en 'aditivosV2.json'.")