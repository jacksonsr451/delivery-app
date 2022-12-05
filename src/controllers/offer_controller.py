from flask import Flask, request

from src.services.offer import OfferServicesInterface


def init_offer_controllers(
    app: Flask, services: OfferServicesInterface
) -> None:
    @app.route('/admin/offers', methods=['POST'])
    def create_offer():
        try:
            services.create(request=request)
        except Exception as error:
            pass

    @app.route('/admin/offers', methods=['PUT'])
    def update_offer():
        try:
            services.update(request=request)
        except Exception as error:
            pass

    @app.route('/admin/offers/<id>', methods=['DELETE'])
    def delete_offer(id):
        try:
            services.delete(id=id)
        except Exception as error:
            pass

    @app.route('/admin/offers', methods=['GET'])
    def show_offer():
        try:
            data = services.show()
        except Exception as error:
            pass

    @app.route('/admin/offers/<id>', methods=['GET'])
    def view_offer(id):
        try:
            data = services.view(id=id)
        except Exception as error:
            pass
