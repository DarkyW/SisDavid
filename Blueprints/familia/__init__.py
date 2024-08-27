from flask import Blueprint

# Inicialización del Blueprint
familia_bp = Blueprint('familia', __name__)

# Importa las rutas asociadas a este Blueprint
from . import routes