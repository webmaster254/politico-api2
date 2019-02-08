from flask import Flask
from instance.config import APP_CONFIG


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(APP_CONFIG[config_name])
    app.config.from_pyfile('config.py')
    from app.api.v1.views import party_view
    app.register_blueprint(office_views.OF)
    app.register_blueprint(party_view.B)
    return app
