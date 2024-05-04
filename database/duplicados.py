import json

# Cargar el archivo JSON
with open('../data/aditivosV2.json', 'r', encoding='utf-8') as file:
    aditivos = json.load(file)

# Crear un diccionario para contar las ocurrencias de cada número
conteo = {}

# Recorrer los aditivos y contar cada número
for aditivo in aditivos:
    numero = aditivo['Numero']
    if numero in conteo:
        conteo[numero] += 1
    else:
        conteo[numero] = 1

# Mostrar los números duplicados
duplicados = {numero: count for numero, count in conteo.items() if count > 1}
print("Números duplicados y sus conteos:", duplicados)