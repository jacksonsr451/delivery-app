from flask import Flask, render_template


class HomeController:
    def __init__(self,app: Flask) -> None:
        @staticmethod
        @app.route('/', methods=['GET'])
        def index() -> str:
            return render_template('pages/index.html')
