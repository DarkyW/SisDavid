from flask import Blueprint

# Inicialización del Blueprint
asistencia_culto_bp = Blueprint('asistencia_culto', __name__)

# Importa las rutas asociadas a este Blueprint
from . import routes