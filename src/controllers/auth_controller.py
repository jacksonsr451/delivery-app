from flask import Flask, redirect, render_template, request, url_for, session

from src.services.auth import AuthServicesInterface


def init_auth_controllers(app: Flask, services: AuthServicesInterface) -> None:
    @app.route('/auth/create-account', methods=['GET'])
    def page_account() -> str:
        return render_template('pages/auth/create_account.html')

    @app.route('/auth/create-account', methods=['POST'])
    def create_account() -> str:
        try:
            services.create(request=request)
            return redirect(url_for('page_login'))
        except Exception as error:
            print(error)
            return redirect(url_for('page_account'))

    @app.route('/auth/login', methods=['GET'])
    def page_login() -> str:
        return render_template('pages/auth/login.html')

    @app.route('/auth/login', methods=['POST'])
    def login() -> str:
        try:
            data = services.login(request=request)
            session['user'] = {'id': data.id, 'username': data.username}
            return redirect(url_for('index'))
        except Exception as error:
            print(error)
            return redirect(url_for('page_login'))

    @app.route('/auth/logout', methods=['GET'])
    def logout() -> str:
        session['user'] = None
        return redirect(url_for('index'))

    @app.route('/auth/validate-email', methods=['GET'])
    def page_validate_email() -> str:
        return render_template('pages/auth/validate_email.html')

    @app.route('/auth/validate-email', methods=['POST'])
    def validate_email() -> str:
        try:
            return redirect(url_for('index'))
        except Exception as error:
            print(error)
            return redirect(url_for('page_validate_email'))
