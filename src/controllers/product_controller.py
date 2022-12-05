from flask import Flask, request

from src.services.product import ProductServicesInterface


def init_product_controllers(
    app: Flask, services: ProductServicesInterface
) -> None:
    @app.route('/admin/products', methods=['POST'])
    def create_product():
        try:
            services.create(request=request)
        except Exception as error:
            pass

    @app.route('/admin/products', methods=['PUT'])
    def update_product():
        try:
            services.update(request=request)
        except Exception as error:
            pass

    @app.route('/admin/products/<id>', methods=['DELETE'])
    def delete_product(id):
        try:
            services.delete(id=id)
        except Exception as error:
            pass

    @app.route('/admin/products', methods=['GET'])
    def show_product():
        try:
            data = services.show()
        except Exception as error:
            pass

    @app.route('/admin/products/<id>', methods=['GET'])
    def view_product(id):
        try:
            data = services.view(id=id)
        except Exception as error:
            pass
