from flask import Blueprint

# Inicialización del Blueprint
personas_bp = Blueprint('personas', __name__)

# Importa las rutas asociadas a este Blueprint
from . import routes