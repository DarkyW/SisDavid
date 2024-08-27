from . import actividades_bp
from flask import request, jsonify
from utils import get_db_connection
import mysql.connector



@actividades_bp.route('/api/actividades', methods=['POST'])
def agregar_actividad():
    datos = request.get_json()
    nombre = datos.get('nombre')    

    if not nombre:
        return jsonify({'error': 'Nombre es obligatorio'}), 400

    fecha_inicio = datos.get('fecha_inicio', None)
    fecha_fin = datos.get('fecha_fin', None)
    descripcion = datos.get('descripcion', None)
    costo = datos.get('costo', None)
    cupo = datos.get('cupo', None)
    

    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO actividad (nombre, fecha_inicio, fecha_fin, descripcion, costo, cupo)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (nombre, fecha_inicio, fecha_fin, descripcion, costo, cupo))
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({'mensaje': 'Actividad agregada exitosamente'}), 201

@actividades_bp.route('/api/actividades', methods=['GET'])
def obtener_actividades():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM actividad")
    actividades = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(actividades)

# Endpoint para actualizar información de una persona por ID
@actividades_bp.route('/api/actividades/<int:id>', methods=['PUT'])
def actualizar_actividad(id):
    datos = request.get_json()

    # Campos opcionales    
    nombre = datos.get('nombre', None)
    fecha_inicio = datos.get('fecha_inicio', None)
    fecha_fin = datos.get('fecha_fin', None)
    descripcion = datos.get('descripcion', None)
    costo = datos.get('costo', None)
    cupo = datos.get('cupo', None)
    id_activo = datos.get('id_activo', None)

    # Verificar que al menos un campo está presente para actualizar
    if not any([nombre, fecha_inicio, fecha_fin, descripcion, costo, cupo, id_activo]):
        return jsonify({'error': 'No hay datos para actualizar'}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    # Construir dinámicamente la consulta SQL para actualizar solo los campos proporcionados
    query = "UPDATE actividad SET "
    params = []
    
    if nombre is not None:
        query += "nombre = %s, "
        params.append(nombre)
    if fecha_inicio is not None:
        query += "fecha_inicio = %s, "
        params.append(fecha_inicio)
    if fecha_fin is not None:
        query += "fecha_fin = %s, "
        params.append(fecha_fin)
    if descripcion is not None:
        query += "descripcion = %s, "
        params.append(descripcion)
    if costo is not None:
        query += "costo = %s, "
        params.append(costo)
    if cupo is not None:
        query += "cupo = %s, "
        params.append(cupo)
    if id_activo is not None:
        query += "id_activo = %s, "
        params.append(id_activo)

    # Eliminar la última coma y espacio ", " de la consulta
    query = query.rstrip(', ')

    # Agregar la cláusula WHERE para seleccionar el registro correcto
    query += " WHERE id_actividad = %s"
    params.append(id)

    cursor.execute(query, params)
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({'mensaje': 'Actividad actualizada exitosamente'}), 200

# Endpoint para eliminar una actividad por ID
@actividades_bp.route('/api/actividades/<int:id>', methods=['DELETE'])
def eliminar_actividad(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "DELETE FROM actividad WHERE id_actividad = %s"
    cursor.execute(query, (id,))
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({'mensaje': 'Actividad eliminada exitosamente'})