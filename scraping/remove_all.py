import json

input_file = '../data/aditivos.json'
output_file = '../data/aditivos_only_number.json'

with open(input_file, 'r', encoding='utf-8') as file:
    aditivos = json.load(file)

aditivos_simplificados = []
for aditivo in aditivos: 
    numero = aditivo['numero']
    aditivo_simplificado = {
        'Numero': numero,
        'es_vegano': False
    }
    aditivos_simplificados.append(aditivo_simplificado)
with open(output_file, 'w', encoding='utf-8') as file:
    json.dump(aditivos_simplificados, file, indent=4, ensure_ascii=False)

print("Cambios aplicados: enlace eliminado y es vegano añadido, en todos como falso")