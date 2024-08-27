from flask import Blueprint

# Inicialización del Blueprint
culto_bp = Blueprint('culto', __name__)

# Importa las rutas asociadas a este Blueprint
from . import routes