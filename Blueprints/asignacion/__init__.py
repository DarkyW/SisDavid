from flask import Blueprint

# Inicialización del Blueprint
asignacion_bp = Blueprint('asignacion', __name__)

# Importa las rutas asociadas a este Blueprint
from . import routes