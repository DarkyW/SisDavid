from . import asistencia_act_bp
from flask import request, jsonify
from utils import get_db_connection

@asistencia_act_bp.route('/api/asistencia_act', methods=['POST'])
def registrar_asistencia():
    datos = request.get_json()
    id_actividad = datos.get('id_actividad')
    id_persona = datos.get('id_persona')

    if not id_actividad or not id_persona:
        return jsonify({'error': 'id_actividad y id_persona son obligatorios'}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    query = "INSERT INTO asistencia_act (id_actividad, id_persona) VALUES (%s, %s)"
    cursor.execute(query, (id_actividad, id_persona))
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({'mensaje': 'Asistencia registrada exitosamente'}), 201

@asistencia_act_bp.route('/api/asistencia_act/persona/<int:id_persona>', methods=['GET'])
def obtener_asistencias_por_persona(id_persona):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT c.* 
    FROM actividad c
    JOIN asistencia_act ac ON c.id_actividad = ac.id_actividad
    WHERE ac.id_persona = %s
    """
    cursor.execute(query, (id_persona,))
    asistencias = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(asistencias)

@asistencia_act_bp.route('/api/asistencia_act/culto/<int:id_actividad>', methods=['GET'])
def obtener_personas_por_actividad(id_actividad):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT p.* 
    FROM persona p
    JOIN asistencia_act ac ON p.id_persona = ac.id_persona
    WHERE ac.id_actividad = %s
    """
    cursor.execute(query, (id_actividad,))
    personas = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(personas)