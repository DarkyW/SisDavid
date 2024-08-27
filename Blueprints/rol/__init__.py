from flask import Blueprint

# Inicialización del Blueprint
rol_bp = Blueprint('rol', __name__)

# Importa las rutas asociadas a este Blueprint
from . import routes