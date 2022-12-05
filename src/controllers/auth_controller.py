from flask import Flask, request, render_template

from src.services.user import UserServicesInterface


def init_auth_controllers(
    app: Flask, services: UserServicesInterface
) -> None:
    @app.route('/auth/create-account', methods=['GET'])
    def index_account() -> str:
        return render_template('pages/auth/create_account.html')

    @app.route('/auth/create-account', methods=['POST'])
    def create_account():
        try:
            services.create(request=request)
        except Exception as error:
            pass

