from flask import Blueprint

# Inicialización del Blueprint
asistencia_act_bp = Blueprint('asistencia_act', __name__)

# Importa las rutas asociadas a este Blueprint
from . import routes