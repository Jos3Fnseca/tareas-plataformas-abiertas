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

#Endpoints para la tarea #3

#Endpoint 1 : obtener todos los estudiantes
@estudiantes_endpoints.route('/estudiantes', methods=['GET'])
def obtener_estudiantes():
    mensaje = "Lista de estudiaantes obtenida correctamente"
    estudiantes = [
        {"nombre": "Juan"},
        {"nombre": "Maria"},
        {"nombre": "Pedro",}
    ]
    return jsonify({"mensaje": mensaje, "estudiantes": estudiantes}), 200

#Endpoint 2 : Agregar un estudiante
@estudiantes_endpoints.route('/agregar_estudiantes', methods=['POST'])
def agregar_estudiante():
    data = request.get_json()
    nombre = data.get('nombre')

    if not nombre :
        return jsonify({'error': 'Faltan datos del estudiante'}), 400

    nuevo_estudiante = {"nombre": nombre}
    mensaje = "Estudiante agregado correctamente:"
    return jsonify({"mensaje": mensaje, "estudiante": nuevo_estudiante}), 201

#Enpoint 3 : Actualizar un estudiante
@estudiantes_endpoints.route('/actualizar_estudiante/<nombre_estudiante>', methods=['PUT'])
def actualizar_estudiante(nombre_estudiante):
    nuevo_estudiante = {'nombre' : nombre_estudiante}
    mensaje = "Estudiante actualizado correctamente"
    return jsonify({"mensaje": mensaje, "estudiante": nuevo_estudiante}), 200

#Endpoint 4 : Eliminar un estudiante
@estudiantes_endpoints.route('/eliminar_estudiante/<nombre_estudiante>', methods=['DELETE'])
def eliminar_estudiante(nombre_estudiante):
    estudiante_eliminado = {'nombre' : nombre_estudiante}
    return jsonify({'message' : f'Estudiante con nombre {nombre_estudiante} eliminado correctamente'}), 200
