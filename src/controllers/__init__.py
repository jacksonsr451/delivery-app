from typing import Any
from flask import Flask

from src.controllers.home_controller import HomeController


def init_controllers(app: Flask, config: dict[str, Any]):
    HomeController(app=app)
