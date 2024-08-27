from . import familia_bp
from flask import request, jsonify
from utils import get_db_connection

#agregar familia
@familia_bp.route('/api/familia', methods=['POST'])
def agregar_familia():
    datos = request.get_json()
    nombre = datos.get('nombre')
    

    if not nombre:
        return jsonify({'error': 'Nombre de la familia es necesario'}), 400
    
    direccion = datos.get('direccion', None)
    telefono = datos.get('telefono', None)
    
    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO familia (nombre, direccion, telefono)
    VALUES (%s, %s, %s)
    """
    cursor.execute(query, (nombre, direccion, telefono))
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({'mensaje': 'familia agregada exitosamente'}), 201

@familia_bp.route('/api/familia', methods=['GET'])
def obtener_familias():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM familia")
    familias = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(familias)

# Endpoint para actualizar información de una persona por ID
@familia_bp.route('/api/familia/<int:id>', methods=['PUT'])
def actualizar_familia(id):
    datos = request.get_json()

    # Campos opcionales    
    nombre = datos.get('nombre', None)
    direccion = datos.get('direccion', None)
    telefono = datos.get('telefono', None)
    

    # Verificar que al menos un campo está presente para actualizar
    if not any([nombre, direccion, telefono]):
        return jsonify({'error': 'No hay datos para actualizar'}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    # Construir dinámicamente la consulta SQL para actualizar solo los campos proporcionados
    query = "UPDATE familia SET "
    params = []    
    
    if nombre is not None:
        query += "nombre = %s, "
        params.append(nombre)
    if direccion is not None:
        query += "direccion = %s, "
        params.append(direccion)
    if telefono is not None:
        query += "telefono = %s, "
        params.append(telefono)
    

    # Eliminar la última coma y espacio ", " de la consulta
    query = query.rstrip(', ')

    # Agregar la cláusula WHERE para seleccionar el registro correcto
    query += " WHERE id_familia = %s"
    params.append(id)

    cursor.execute(query, params)
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({'mensaje': 'familia actualizada exitosamente'}), 200

# Endpoint para eliminar una familia por ID
@familia_bp.route('/api/familia/<int:id>', methods=['DELETE'])
def eliminar_familia(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "DELETE FROM familia WHERE id_familia = %s"
    cursor.execute(query, (id,))
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({'mensaje': 'Familia eliminada exitosamente'})