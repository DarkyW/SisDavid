from . import asistencia_culto_bp
from flask import request, jsonify
from utils import get_db_connection

@asistencia_culto_bp.route('/api/asistencia_culto', methods=['POST'])
def registrar_asistencia():
    datos = request.get_json()
    id_culto = datos.get('id_culto')
    id_persona = datos.get('id_persona')

    if not id_culto or not id_persona:
        return jsonify({'error': 'id_culto y id_persona son obligatorios'}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    query = "INSERT INTO asistencia_culto (id_culto, id_persona) VALUES (%s, %s)"
    cursor.execute(query, (id_culto, id_persona))
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({'mensaje': 'Asistencia registrada exitosamente'}), 201

@asistencia_culto_bp.route('/api/asistencia_culto/persona/<int:id_persona>', methods=['GET'])
def obtener_asistencias_por_persona(id_persona):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT c.* 
    FROM culto c
    JOIN asistencia_culto ac ON c.id_culto = ac.id_culto
    WHERE ac.id_persona = %s
    """
    cursor.execute(query, (id_persona,))
    asistencias = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(asistencias)

@asistencia_culto_bp.route('/api/asistencia_culto/culto/<int:id_culto>', methods=['GET'])
def obtener_personas_por_culto(id_culto):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT p.* 
    FROM persona p
    JOIN asistencia_culto ac ON p.id_persona = ac.id_persona
    WHERE ac.id_culto = %s
    """
    cursor.execute(query, (id_culto,))
    personas = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(personas)