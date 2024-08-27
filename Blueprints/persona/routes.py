from . import personas_bp
from flask import request, jsonify
from utils import get_db_connection
import mysql.connector



@personas_bp.route('/api/personas', methods=['POST'])
def agregar_persona():
    datos = request.get_json()
    nombre = datos.get('nombre')
    apellido = datos.get('apellido')

    if not nombre or not apellido:
        return jsonify({'error': 'Nombre y apellido son obligatorios'}), 400

    rut = datos.get('rut', None)
    fecha_baut = datos.get('fecha_baut', None)
    correo = datos.get('correo', None)
    telefono = datos.get('telefono', None)
    ocupacion = datos.get('ocupacion', None)
    fecha_nac = datos.get('fecha_nac', None)

    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO persona (nombre, apellido, rut, fecha_baut, correo, telefono, ocupacion, fecha_nac)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (nombre, apellido, rut, fecha_baut, correo, telefono, ocupacion, fecha_nac))
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({'mensaje': 'Persona agregada exitosamente'}), 201

@personas_bp.route('/api/personas', methods=['GET'])
def obtener_personas():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM persona")
    personas = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(personas)

# Endpoint para actualizar información de una persona por ID
@personas_bp.route('/api/personas/<int:id>', methods=['PUT'])
def actualizar_persona(id):
    datos = request.get_json()

    # Campos opcionales
    rut = datos.get('rut', None)
    nombre = datos.get('nombre', None)
    apellido = datos.get('apellido', None)
    fecha_baut = datos.get('fecha_baut', None)
    correo = datos.get('correo', None)
    telefono = datos.get('telefono', None)
    ocupacion = datos.get('ocupacion', None)
    fecha_nac = datos.get('fecha_nac', None)

    # Verificar que al menos un campo está presente para actualizar
    if not any([rut, nombre, apellido, fecha_baut, correo, telefono, ocupacion, fecha_nac]):
        return jsonify({'error': 'No hay datos para actualizar'}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    # Construir dinámicamente la consulta SQL para actualizar solo los campos proporcionados
    query = "UPDATE persona SET "
    params = []
    
    if rut is not None:
        query += "rut = %s, "
        params.append(rut)
    if nombre is not None:
        query += "nombre = %s, "
        params.append(nombre)
    if apellido is not None:
        query += "apellido = %s, "
        params.append(apellido)
    if fecha_baut is not None:
        query += "fecha_baut = %s, "
        params.append(fecha_baut)
    if correo is not None:
        query += "correo = %s, "
        params.append(correo)
    if telefono is not None:
        query += "telefono = %s, "
        params.append(telefono)
    if ocupacion is not None:
        query += "ocupacion = %s, "
        params.append(ocupacion)
    if fecha_nac is not None:
        query += "fecha_nac = %s, "
        params.append(fecha_nac)

    # Eliminar la última coma y espacio ", " de la consulta
    query = query.rstrip(', ')

    # Agregar la cláusula WHERE para seleccionar el registro correcto
    query += " WHERE id_persona = %s"
    params.append(id)

    cursor.execute(query, params)
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({'mensaje': 'Persona actualizada exitosamente'}), 200

# Endpoint para eliminar una persona por ID
@personas_bp.route('/api/personas/<int:id>', methods=['DELETE'])
def eliminar_persona(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "DELETE FROM persona WHERE id_persona = %s"
    cursor.execute(query, (id,))
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({'mensaje': 'Persona eliminada exitosamente'})