from . import culto_bp
from flask import request, jsonify
from utils import get_db_connection

#agregar culto
@culto_bp.route('/api/culto', methods=['POST'])
def agregar_culto():
    datos = request.get_json()
    fecha = datos.get('fecha')
    

    if not fecha:
        return jsonify({'error': 'fecha del culto es necesario'}), 400
    
    predicador = datos.get('predicador', None)   
    
    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO culto (fecha, predicador)
    VALUES (%s, %s)
    """
    cursor.execute(query, (fecha, predicador))
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({'mensaje': 'culto agregado exitosamente'}), 201

@culto_bp.route('/api/culto', methods=['GET'])
def obtener_culto():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM culto")
    cultos = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(cultos)

# Endpoint para actualizar información de un culto por ID
@culto_bp.route('/api/culto/<int:id>', methods=['PUT'])
def actualizar_culto(id):
    datos = request.get_json()

    # Campos opcionales    
    fecha = datos.get('fecha', None)
    predicador = datos.get('predicador', None)
    
    

    # Verificar que al menos un campo está presente para actualizar
    if not any([fecha, predicador]):
        return jsonify({'error': 'No hay datos para actualizar'}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    # Construir dinámicamente la consulta SQL para actualizar solo los campos proporcionados
    query = "UPDATE culto SET "
    params = []    
    
    if fecha is not None:
        query += "fecha = %s, "
        params.append(fecha)
    if predicador is not None:
        query += "predicador = %s, "
        params.append(predicador)    
    

    # Eliminar la última coma y espacio ", " de la consulta
    query = query.rstrip(', ')

    # Agregar la cláusula WHERE para seleccionar el registro correcto
    query += " WHERE id_culto = %s"
    params.append(id)

    cursor.execute(query, params)
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({'mensaje': 'culto actualizado exitosamente'}), 200

# Endpoint para eliminar una familia por ID
@culto_bp.route('/api/culto/<int:id>', methods=['DELETE'])
def eliminar_culto(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "DELETE FROM culto WHERE id_culto = %s"
    cursor.execute(query, (id,))
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({'mensaje': 'Culto eliminado exitosamente'})