import sqlite3
import json
#Caragamos el archivo json version 2 
with open('../data/aditivosV2.json', 'r', encoding='utf-8') as file:
    aditivos = json.load(file)
#Abrimos la conexion a la base de datos
conn = sqlite3.connect('aditivosV2.0.db')
c = conn.cursor()
#Insertamos los datos del json version 2 en la base datos 
for aditivo in aditivos:
    c.execute('''
    INSERT INTO aditivos (numero, clasificacion, enlace_numero, enlace_informacion, definicion)
    VALUES (?, ?, ?, ?, ?)
    ''', (aditivo['Numero'], aditivo['Clasificacion_Vegana'], aditivo['Enlace_Numero'], aditivo['Enlace_Nombre'], aditivo['Definicion']))
#Confirmamos los cambios y cerramos la conexion.
conn.commit()
conn.close()
print("Datos insertados con exito")