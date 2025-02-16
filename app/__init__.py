from flask import Flask


def create_app():
    app = Flask(__name__)

    # Importa e registra as rotas
    from app.routes.api_routes import bp

    app.register_blueprint(bp)

    return app
