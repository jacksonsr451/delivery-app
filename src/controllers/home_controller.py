from flask import Flask, render_template


def home_controller(app: Flask) -> None:
    @app.route('/', methods=['GET'])
    def index() -> str:
        return render_template('pages/index.html')
