from flask import Flask, redirect, render_template, request

from src.services.auth import AuthServicesInterface


def init_auth_controllers(app: Flask, services: AuthServicesInterface) -> None:
    @app.route('/auth/create-account', methods=['GET'])
    def index_account() -> str:
        return render_template('pages/auth/create_account.html')

    @app.route('/auth/create-account', methods=['POST'])
    def create_account() -> str:
        try:
            services.create(request=request)
            return redirect('login')
        except Exception as error:
            return redirect('index_account')

    @app.route('/auth/login', methods=['GET'])
    def login() -> str:
        return render_template('pages/auth/login.html')
