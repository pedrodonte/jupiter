from flask import Flask, request, jsonify
from .autorizacion import (
    select_by_beneficiario,
    cambiar_estado,
    crear_registro_autorizacion,
    consultar_por_id,
)

app = Flask(__name__)


@app.route("/autorizacion/<beneficiario>/<estado>", methods=["GET"])
def autorizacion(beneficiario, estado):
    return jsonify(select_by_beneficiario(beneficiario, estado))


@app.route("/autorizacion/cambio-estado", methods=["POST"])
def cambio_estado():
    try:
        data = request.get_json()
        id_autorizacion = data["id"]
        nuevo_estado = data["estado"]
        cambiar_estado(id_autorizacion, nuevo_estado)
        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})


@app.route("/autorizacion/crear", methods=["POST"])
def crear():
    try:
        data = request.get_json()

        nuevo_id = crear_registro_autorizacion(data)
        return jsonify({"success": True, "id": nuevo_id})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})


@app.route("/autorizacion/consultar/<id_autorizacion>", methods=["GET"])
def consultar(id_autorizacion):
    try:
        return jsonify(consultar_por_id(id_autorizacion))
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})
