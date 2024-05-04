import sqlite3
#conexion a la base de datos SQLite
conn = sqlite3.connect('aditivosV2.db')
c = conn.cursor()
#creamos la tabla
c.execute('''
CREATE TABLE IF NOT EXISTS aditivos (
    numero TEXT PRIMARY KEY,
    clasificacion TEXT,
    enlace_numero TEXT,
    enlace_informacion TEXT
)
''')

print("Tabla creada con exito.")

conn.commit()
conn.close()