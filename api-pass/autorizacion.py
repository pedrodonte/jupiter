# Import module
import sqlite3
import os
from datetime import datetime
from uuid import uuid4

# estructura_autorizacion
# beneficiario VARCHAR(255) NOT NULL,
# fecha_creacion datetime NOT NULL,
# fecha_aprobacion datetime  NULL,
# estado varchar(255) NOT NULL,
# descripcion varchar(255) NOT NULL

# Connecting to sqlite
# connection object
ARCHIVO_SQLITE = os.getenv("ARCHIVO_SQLITE")
if ARCHIVO_SQLITE is None:
    raise ValueError("ARCHIVO_SQLITE no esta definido")


def crear_registro_autorizacion(registro_nuevo):
    # cursor object
    connection_obj = sqlite3.connect(ARCHIVO_SQLITE)
    time_stamp = datetime.now()
    registro_nuevo["fecha_creacion"] = time_stamp
    registro_nuevo["id"] = str(uuid4()).replace("-", "")
    registro_nuevo["beneficiario"] = registro_nuevo["beneficiario"].upper()
    cursor_obj = connection_obj.cursor()
    # Inserting data into table
    cursor_obj.execute(
        "INSERT INTO autorizacion (id, beneficiario, fecha_creacion, estado, descripcion) VALUES (:id, :beneficiario, :fecha_creacion, :estado, :descripcion)",
        registro_nuevo,
    )
    # Commit the transaction
    connection_obj.commit()
    # Close the connection
    connection_obj.close()


def select_by_beneficiario(beneficiario, estado):
    # cursor object
    beneficiario = beneficiario.upper()
    connection_obj = sqlite3.connect(ARCHIVO_SQLITE)
    cursor_obj = connection_obj.cursor()
    # Inserting data into table
    cursor_obj.execute(
        "SELECT * FROM autorizacion WHERE beneficiario = :beneficiario and estado = :estado",
        {"beneficiario": beneficiario, "estado": estado},
    )
    headers = [i[0] for i in cursor_obj.description]
    registros = [dict(zip(headers, row)) for row in cursor_obj.fetchall()]
    cursor_obj.close()
    return registros


def cambiar_estado(id_autorizacion, nuevo_estado):
    # cursor object
    connection_obj = sqlite3.connect(ARCHIVO_SQLITE)
    cursor_obj = connection_obj.cursor()
    fecha_aprobacion = datetime.now()
    # Inserting data into table
    cursor_obj.execute(
        "UPDATE autorizacion SET estado = :estado, fecha_aprobacion=:fecha_aprobacion WHERE id = :id_autorizacion",
        {
            "estado": nuevo_estado,
            "id_autorizacion": id_autorizacion,
            "fecha_aprobacion": fecha_aprobacion,
        },
    )
    # Commit the transaction
    connection_obj.commit()
    # Close the connection
    connection_obj.close()


nuevo_registro = {
    "beneficiario": "Juan",
    "estado": "Pendiente",
    "descripcion": "Aprobado por el jefe",
    "id": str(uuid4()).replace("-", ""),
}
