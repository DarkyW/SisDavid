from flask import Blueprint

# Inicialización del Blueprint
actividades_bp = Blueprint('actividades', __name__)

# Importa las rutas asociadas a este Blueprint
from . import routes