from flask import Flask
from Blueprints.persona import personas_bp
from Blueprints.familia import familia_bp
from Blueprints.culto import culto_bp
from Blueprints.actividad import actividades_bp
from Blueprints.asignacion import asignacion_bp
from Blueprints.asistencia_act import asistencia_act_bp
from Blueprints.asistencia_culto import asistencia_culto_bp
from Blueprints.celula import celula_bp
from Blueprints.reserva_act import reserva_act_bp
from Blueprints.rol import rol_bp
from Blueprints.usuario import usuario_bp


app = Flask(__name__)
app.register_blueprint(personas_bp)
app.register_blueprint(familia_bp)
app.register_blueprint(culto_bp)
app.register_blueprint(actividades_bp)
app.register_blueprint(asignacion_bp)
app.register_blueprint(asistencia_act_bp)
app.register_blueprint(asistencia_culto_bp)
app.register_blueprint(celula_bp)
app.register_blueprint(reserva_act_bp)
app.register_blueprint(rol_bp)
app.register_blueprint(usuario_bp)



if __name__ == '__main__':
    app.run(debug=True)