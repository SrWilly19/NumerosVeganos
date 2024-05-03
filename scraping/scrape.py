import requests
from bs4 import BeautifulSoup
import json
url = 'https://www.aditivos-alimentarios.com/'
response = requests.get(url)
data_to_save = []

if response.status_code == 200:
    print("Solicitud exitosa!")
    soup = BeautifulSoup(response.text, 'html.parser')
    tabla = soup.find('table')
    if tabla:
        filas = tabla.find_all('tr')[1:]
        for fila in filas:
            celdas = fila.find_all('td')
            if len(celdas) == 3:
                numero = celdas[0].find('a').get_text(strip=True)
                enlace_numero = celdas[0].find('a')['href']
                nombre = celdas[1].find('a').get_text(strip=True)
                toxicidad = celdas[2].find('span').get_text(strip=True)
                data_to_save.append({
                    'numero': numero,
                    'nombre': nombre,
                    'toxicidad': toxicidad,
                    'enlace_numero': enlace_numero
                })
    else:
        print(f"Error en la solicitud: {response.status_code}")

with open('../data/aditivos.json', 'w', encoding='utf-8') as file:
    json.dump(data_to_save, file, ensure_ascii=False, indent=4)
            


