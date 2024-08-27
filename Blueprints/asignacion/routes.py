from . import asignacion_bp
from flask import request, jsonify
from utils import get_db_connection

@asignacion_bp.route('/api/asignacion', methods=['POST'])
def crear_asignacion():
    datos = request.get_json()

    descripcion = datos.get('descripcion')
    id_usuario = datos.get('id_usuario')
    id_rol = datos.get('id_rol')

    if not descripcion or not id_usuario or not id_rol:
        return jsonify({'error': 'Todos los campos son obligatorios'}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO asignacion (descripcion, id_usuario, id_rol)
    VALUES (%s, %s, %s)
    """
    cursor.execute(query, (descripcion, id_usuario, id_rol))
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({'mensaje': 'Asignación creada exitosamente'}), 201

@asignacion_bp.route('/api/asignacion', methods=['GET'])
def obtener_asignaciones():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    query = "SELECT * FROM asignacion"
    cursor.execute(query)
    asignaciones = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(asignaciones)

@asignacion_bp.route('/api/asignacion/<int:id_asig>', methods=['PUT'])
def actualizar_asignacion(id_asig):
    datos = request.get_json()

    descripcion = datos.get('descripcion')
    id_usuario = datos.get('id_usuario')
    id_rol = datos.get('id_rol')

    if not any([descripcion, id_usuario, id_rol]):
        return jsonify({'error': 'Se requiere al menos un campo para actualizar'}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    query = "UPDATE asignacion SET "
    params = []

    if descripcion is not None:
        query += "descripcion = %s, "
        params.append(descripcion)
    if id_usuario is not None:
        query += "id_usuario = %s, "
        params.append(id_usuario)
    if id_rol is not None:
        query += "id_rol = %s, "
        params.append(id_rol)

    query = query.rstrip(', ')
    query += " WHERE id_asig = %s"
    params.append(id_asig)

    cursor.execute(query, params)
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({'mensaje': 'Asignación actualizada exitosamente'}), 200

@asignacion_bp.route('/api/asignacion/<int:id_asig>', methods=['DELETE'])
def eliminar_asignacion(id_asig):
    conn = get_db_connection()
    cursor = conn.cursor()

    query = "DELETE FROM asignacion WHERE id_asig = %s"
    cursor.execute(query, (id_asig,))
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({'mensaje': 'Asignación eliminada exitosamente'}), 200