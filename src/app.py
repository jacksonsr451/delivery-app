from flask import Flask

from src.controllers import init_controllers
from .core.config import config

def create_app() -> Flask:
    app = Flask(__name__, template_folder='views', static_folder='../public')
    init_controllers(app=app, config=config)
    return app
