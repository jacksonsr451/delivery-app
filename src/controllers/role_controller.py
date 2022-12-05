from flask import Flask, request

from src.services.role import RoleServicesInterface


def init_role_controllers(
    app: Flask, services: RoleServicesInterface
) -> None:
    @app.route('/admin/roles', methods=['POST'])
    def create_role():
        try:
            services.create(request=request)
        except Exception as error:
            pass

    @app.route('/admin/roles', methods=['PUT'])
    def update_role():
        try:
            services.update(request=request)
        except Exception as error:
            pass

    @app.route('/admin/roles/<id>', methods=['DELETE'])
    def delete_role(id):
        try:
            services.delete(id=id)
        except Exception as error:
            pass

    @app.route('/admin/roles', methods=['GET'])
    def show_role():
        try:
            data = services.show()
        except Exception as error:
            pass

    @app.route('/admin/roles/<id>', methods=['GET'])
    def view_role(id):
        try:
            data = services.view(id=id)
        except Exception as error:
            pass
