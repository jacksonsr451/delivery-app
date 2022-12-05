from flask import Flask, request

from src.services.contact import ContactServicesInterface


def init_contact_controllers(
    app: Flask, services: ContactServicesInterface
) -> None:
    @app.route('/admin/contactes', methods=['POST'])
    def create_contact():
        try:
            services.create(request=request)
        except Exception as error:
            pass

    @app.route('/admin/contacts', methods=['PUT'])
    def update_contact():
        try:
            services.update(request=request)
        except Exception as error:
            pass

    @app.route('/admin/contacts/<id>', methods=['DELETE'])
    def delete_contact(id):
        try:
            services.delete(id=id)
        except Exception as error:
            pass

    @app.route('/admin/contacts', methods=['GET'])
    def show_contact():
        try:
            data = services.show()
        except Exception as error:
            pass

    @app.route('/admin/contacts/<id>', methods=['GET'])
    def view_contact(id):
        try:
            data = services.view(id=id)
        except Exception as error:
            pass
