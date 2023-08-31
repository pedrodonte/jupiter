$env:ARCHIVO_SQLITE="C:\dev\jupiter\autorizaciones.db"
$env:FLASK_APP="api-pass:app"
$env:FLASK_ENV="development"
python api-pass/crear_tabla.py
flask run --host=0.0.0.0