from flask import Blueprint, request,jsonify

estudiantes_endpoints = Blueprint('estudiantes', __name__)

@estudiantes_endpoints.route('/hola', methods=['GET'])
def holamundo():
    return jsonify({"message": "¡Bienvenidos nuevos estudiantes!"}), 200

@estudiantes_endpoints.route('/saludo', methods=['GET'])
def saludar():
    data = request.get_json()
    nombre = data.get('nombre')
    apellido = data.get('apellido')
    if not nombre or not apellido:
        return jsonify({'error': 'Debe ingresar el nombre del estudiante'}), 400

    saludo = f"Hola {nombre} {apellido}"
    return jsonify({'saludo': saludo}), 200