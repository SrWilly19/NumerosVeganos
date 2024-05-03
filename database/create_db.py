import sqlite3

conn = sqlite3.connect('aditivos.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS aditivos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    numero TEXT UNIQUE,
    nombre TEXT,
    toxicidad TEXT,
    es_vegano BOOLEAN
)
''')

print("Tabla creada con exito.")

conn.commit()
conn.close()