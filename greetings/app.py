from flask import Flask
from greetings.health import health
from greetings.greetings_generator import greet


def create():
    app = Flask(__name__)
    app.register_blueprint(health)
    app.register_blueprint(greet)
    return app
