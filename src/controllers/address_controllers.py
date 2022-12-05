from flask import Flask, request

from src.services.address import AddressServicesInterface


def init_address_controllers(
    app: Flask, services: AddressServicesInterface
) -> None:
    @app.route('/admin/address', methods=['POST'])
    def create_address():
        try:
            services.create(request=request)
        except Exception as error:
            pass

    @app.route('/admin/address', methods=['PUT'])
    def update_address():
        try:
            services.update(request=request)
        except Exception as error:
            pass

    @app.route('/admin/address/<id>', methods=['DELETE'])
    def delete_address(id):
        try:
            services.delete(id=id)
        except Exception as error:
            pass

    @app.route('/admin/address', methods=['GET'])
    def show_address():
        try:
            data = services.show()
        except Exception as error:
            pass

    @app.route('/admin/address/<id>', methods=['GET'])
    def view_address(id):
        try:
            data = services.view(id=id)
        except Exception as error:
            pass
