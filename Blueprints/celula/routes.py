from . import celula_bp
from flask import request, jsonify
from utils import get_db_connection

#agregar 
@celula_bp.route('/api/celula', methods=['POST'])
def agregar_celula():
    datos = request.get_json()        
    nombre = datos.get('nombre', None)   
    
    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO celula (nombre)
    VALUES (%s, %s)
    """
    cursor.execute(query, (nombre))
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({'mensaje': 'celula agregada exitosamente'}), 201

@celula_bp.route('/api/celula', methods=['GET'])
def obtener_celula():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM celula")
    celulas = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(celulas)

# Endpoint para actualizar información de un celula por ID
@celula_bp.route('/api/celula/<int:id>', methods=['PUT'])
def actualizar_celula(id):
    datos = request.get_json()

    # Campos opcionales    
    nombre = datos.get('nombre', None)
    
    
    

    # Verificar que al menos un campo está presente para actualizar
    if not any([nombre]):
        return jsonify({'error': 'No hay datos para actualizar'}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    # Construir dinámicamente la consulta SQL para actualizar solo los campos proporcionados
    query = "UPDATE celula SET "
    params = []    
    
    if nombre is not None:
        query += "nombre = %s, "
        params.append(nombre)        
    

    # Eliminar la última coma y espacio ", " de la consulta
    query = query.rstrip(', ')

    # Agregar la cláusula WHERE para seleccionar el registro correcto
    query += " WHERE id_celula = %s"
    params.append(id)

    cursor.execute(query, params)
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({'mensaje': 'celula actualizado exitosamente'}), 200

# Endpoint para eliminar una celula por ID
@celula_bp.route('/api/celula/<int:id>', methods=['DELETE'])
def eliminar_culto(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "DELETE FROM celula WHERE id_celula = %s"
    cursor.execute(query, (id,))
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({'mensaje': 'Celula eliminado exitosamente'})