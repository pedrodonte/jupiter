# Import module
import sqlite3
import os

# Connecting to sqlite
# connection object
ARCHIVO_SQLITE = os.getenv("ARCHIVO_SQLITE")
if ARCHIVO_SQLITE is None:
    raise ValueError("ARCHIVO_SQLITE no esta definido")

try:
    connection_obj = sqlite3.connect(ARCHIVO_SQLITE)
    # cursor object
    cursor_obj = connection_obj.cursor()
    # Drop the GEEK table if already exists.
    cursor_obj.execute("DROP TABLE IF EXISTS autorizacion")
    # Creating table
    table = """ CREATE TABLE autorizacion (
                id varchar(255) PRIMARY KEY,
                beneficiario VARCHAR(255) NOT NULL,
                fecha_creacion datetime NOT NULL,
                fecha_aprobacion datetime NULL,
                estado varchar(255) NOT NULL,
                descripcion varchar(255) NOT NULL
            ); """
    cursor_obj.execute(table)
    print("Table is Ready")
    # Close the connection
    connection_obj.close()

except Exception as e:
    print(e)
