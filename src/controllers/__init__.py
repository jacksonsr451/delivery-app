from typing import Any

from flask import Flask

from src.controllers.address_controllers import init_address_controllers

from .home_controller import home_controller


def init_controllers(app: Flask, config: dict[str, Any]):
    home_controller(app=app)
    init_address_controllers(
        app=app, services=config['services']['AddressServices']
    )
