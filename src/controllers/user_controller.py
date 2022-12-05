from flask import Flask, request

from src.services.user import UserServicesInterface


def init_user_controllers(app: Flask, services: UserServicesInterface) -> None:
    @app.route('/admin/users', methods=['POST'])
    def create_user():
        try:
            services.create(request=request)
        except Exception as error:
            pass

    @app.route('/admin/users', methods=['PUT'])
    def update_user():
        try:
            services.update(request=request)
        except Exception as error:
            pass

    @app.route('/admin/users/<id>', methods=['DELETE'])
    def delete_user(id):
        try:
            services.delete(id=id)
        except Exception as error:
            pass

    @app.route('/admin/users', methods=['GET'])
    def show_user():
        try:
            data = services.show()
        except Exception as error:
            pass

    @app.route('/admin/users/<id>', methods=['GET'])
    def view_user(id):
        try:
            data = services.view(id=id)
        except Exception as error:
            pass
