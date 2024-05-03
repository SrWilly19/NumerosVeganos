import json

input_file = '../data/aditivos.json'
output_file = '../data/aditivos_modificados.json'

with open(input_file, 'r', encoding='utf-8') as file:
    aditivos = json.load(file)

for aditivo in aditivos: 
    if 'enlace_numero' in aditivo:
        del aditivo['enlace_numero']
    aditivo['es_vegano'] = False

with open(output_file, 'w', encoding='utf-8') as file:
    json.dump(aditivos, file, indent=4)

print("Cambios aplicados: enlace eliminado y es vegano añadido, en todos como falso")