from flask import Flask, redirect, render_template, request, url_for, session


def init_shopping_card(app: Flask): 
    @app.route('/shopping/card')
    def page_card() -> str:
        return render_template('pages/shopping/card.html')
