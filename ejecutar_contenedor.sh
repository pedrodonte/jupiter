export ARCHIVO_SQLITE=/opt/base_datos.db
export FLASK_APP=api-pass:app
export FLASK_ENV=development
python api-pass/crear_tabla.py
flask run --host=0.0.0.0
