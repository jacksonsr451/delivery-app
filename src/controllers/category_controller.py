from flask import Flask, request

from src.services.category import CategoryServicesInterface


def init_category_controllers(
    app: Flask, services: CategoryServicesInterface
) -> None:
    @app.route('/admin/categories', methods=['POST'])
    def create_category():
        try:
            services.create(request=request)
        except Exception as error:
            pass

    @app.route('/admin/categories', methods=['PUT'])
    def update_category():
        try:
            services.update(request=request)
        except Exception as error:
            pass

    @app.route('/admin/categories/<id>', methods=['DELETE'])
    def delete_category(id):
        try:
            services.delete(id=id)
        except Exception as error:
            pass

    @app.route('/admin/categories', methods=['GET'])
    def show_category():
        try:
            data = services.show()
        except Exception as error:
            pass

    @app.route('/admin/categories/<id>', methods=['GET'])
    def view_category(id):
        try:
            data = services.view(id=id)
        except Exception as error:
            pass
