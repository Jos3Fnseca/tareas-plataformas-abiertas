from flask import Flask
from flask_cors import CORS
from .controllers.estudiantes import estudiantes_endpoints

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.register_blueprint(estudiantes_endpoints, url_prefix='/estudiantes/api/v1')
    CORS(app, origins="*")
    return app

