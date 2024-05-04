import sqlite3
#Conectar la base de datos aditivosV2
conn = sqlite3.connect('../database/aditivosV2.db')
c = conn.cursor()
#Realizamos una consulta SQL, seleccionando los 5 primeros registros de nuestra tabla aditivos
try:
    c.execute('SELECT * FROM aditivos LIMIT 5')
    rows = c.fetchall()
    for row in rows:
        print(row)
except Exception as e:
    print("Ocurrio un error al realizar la consulta: ", e)

#Cerramos la conexion a la base de datos
conn.close()