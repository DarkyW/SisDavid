from . import rol_bp
from flask import request, jsonify
from utils import get_db_connection

@rol_bp.route('/api/rol', methods=['POST'])
def crear_rol():
    datos = request.get_json()

    nombre_rol = datos.get('nombre_rol')
    descripcion = datos.get('descripcion')

    if not nombre_rol:
        return jsonify({'error': 'El nombre del rol es obligatorio'}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    query = "INSERT INTO rol (nombre_rol, descripcion) VALUES (%s, %s)"
    cursor.execute(query, (nombre_rol, descripcion))
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({'mensaje': 'Rol creado exitosamente'}), 201

@rol_bp.route('/api/rol', methods=['GET'])
def obtener_roles():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    query = "SELECT * FROM rol"
    cursor.execute(query)
    roles = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(roles)

@rol_bp.route('/api/rol/<int:id_rol>', methods=['GET'])
def obtener_rol_por_id(id_rol):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    query = "SELECT * FROM rol WHERE id_rol = %s"
    cursor.execute(query, (id_rol,))
    rol = cursor.fetchone()

    cursor.close()
    conn.close()

    if rol:
        return jsonify(rol)
    else:
        return jsonify({'error': 'Rol no encontrado'}), 404
    
@rol_bp.route('/api/rol/<int:id_rol>', methods=['PUT'])
def actualizar_rol(id_rol):
    datos = request.get_json()

    nombre_rol = datos.get('nombre_rol')
    descripcion = datos.get('descripcion')

    if not any([nombre_rol, descripcion]):
        return jsonify({'error': 'Se requiere al menos un campo para actualizar'}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    query = "UPDATE rol SET "
    params = []

    if nombre_rol is not None:
        query += "nombre_rol = %s, "
        params.append(nombre_rol)
    if descripcion is not None:
        query += "descripcion = %s, "
        params.append(descripcion)

    query = query.rstrip(', ')
    query += " WHERE id_rol = %s"
    params.append(id_rol)

    cursor.execute(query, params)
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({'mensaje': 'Rol actualizado exitosamente'}), 200

@rol_bp.route('/api/rol/<int:id_rol>', methods=['DELETE'])
def eliminar_rol(id_rol):
    conn = get_db_connection()
    cursor = conn.cursor()

    query = "DELETE FROM rol WHERE id_rol = %s"
    cursor.execute(query, (id_rol,))
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({'mensaje': 'Rol eliminado exitosamente'}), 200
