from . import usuario_bp
from flask import request, jsonify
from utils import get_db_connection

@usuario_bp.route('/api/usuario', methods=['POST'])
def crear_usuario():
    datos = request.get_json()

    id_persona = datos.get('id_persona')
    nombre_us = datos.get('nombre_us')
    password = datos.get('password')
    permisos = datos.get('permisos')

    if not id_persona or not nombre_us or not password:
        return jsonify({'error': 'id_persona, nombre_us y password son obligatorios'}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    query = "INSERT INTO usuario (id_persona, nombre_us, password, permisos) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (id_persona, nombre_us, password, permisos))
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({'mensaje': 'Usuario creado exitosamente'}), 201
@usuario_bp.route('/api/usuario', methods=['GET'])
def obtener_usuarios():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    query = "SELECT * FROM usuario"
    cursor.execute(query)
    usuarios = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(usuarios)

@usuario_bp.route('/api/usuario/<int:id_rol>', methods=['GET'])
def obtener_usuario_por_id(id_usuario):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    query = "SELECT * FROM usuario WHERE id_usuario = %s"
    cursor.execute(query, (id_usuario,))
    usuario = cursor.fetchone()

    cursor.close()
    conn.close()

    if usuario:
        return jsonify(usuario)
    else:
        return jsonify({'error': 'Usuario no encontrado'}), 404
    
@usuario_bp.route('/api/usuario/<int:id_rol>', methods=['PUT'])
def actualizar_usuario(id_usuario):
    datos = request.get_json()

    id_persona = datos.get('id_persona')
    nombre_us = datos.get('nombre_us')
    password = datos.get('password')
    permisos = datos.get('permisos')

    if not any([id_persona, nombre_us, password, permisos]):
        return jsonify({'error': 'Se requiere al menos un campo para actualizar'}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    query = "UPDATE usuario SET "
    params = []

    if id_persona is not None:
        query += "id_persona = %s, "
        params.append(id_persona)
    if nombre_us is not None:
        query += "nombre_us = %s, "
        params.append(nombre_us)
    if password is not None:
        query += "password = %s, "
        params.append(password)
    if permisos is not None:
        query += "permisos = %s, "
        params.append(permisos)

    query = query.rstrip(', ')
    query += " WHERE id_usuario = %s"
    params.append(id_usuario)

    cursor.execute(query, params)
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({'mensaje': 'Usuario actualizado exitosamente'}), 200

@usuario_bp.route('/api/usuario/<int:id_rol>', methods=['DELETE'])
def eliminar_usuario(id_usuario):
    conn = get_db_connection()
    cursor = conn.cursor()

    query = "DELETE FROM usuario WHERE id_usuario = %s"
    cursor.execute(query, (id_usuario,))
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({'mensaje': 'Usuario eliminado exitosamente'}), 200
