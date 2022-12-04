from typing import Any
from flask import Flask

from .home_controller import home_controller


def init_controllers(app: Flask, config: dict[str, Any]):
    home_controller(app=app)
