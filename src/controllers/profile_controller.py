from flask import Flask, request

from src.services.profile import ProfileServicesInterface


def init_profile_controllers(
    app: Flask, services: ProfileServicesInterface
) -> None:
    @app.route('/admin/profiles', methods=['POST'])
    def create_profile():
        try:
            services.create(request=request)
        except Exception as error:
            pass

    @app.route('/admin/profiles', methods=['PUT'])
    def update_profile():
        try:
            services.update(request=request)
        except Exception as error:
            pass

    @app.route('/admin/profiles/<id>', methods=['DELETE'])
    def delete_profile(id):
        try:
            services.delete(id=id)
        except Exception as error:
            pass

    @app.route('/admin/profiles', methods=['GET'])
    def show_profile():
        try:
            data = services.show()
        except Exception as error:
            pass

    @app.route('/admin/profiles/<id>', methods=['GET'])
    def view_profile(id):
        try:
            data = services.view(id=id)
        except Exception as error:
            pass
