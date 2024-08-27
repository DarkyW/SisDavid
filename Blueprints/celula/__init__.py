from flask import Blueprint

# Inicialización del Blueprint
celula_bp = Blueprint('celula', __name__)

# Importa las rutas asociadas a este Blueprint
from . import routes