from flask import Blueprint

# Inicialización del Blueprint
usuario_bp = Blueprint('usuario', __name__)

# Importa las rutas asociadas a este Blueprint
from . import routes