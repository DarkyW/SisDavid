from flask import Blueprint

# Inicialización del Blueprint
reserva_act_bp = Blueprint('reserva_act', __name__)

# Importa las rutas asociadas a este Blueprint
from . import routes