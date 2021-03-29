from flask import jsonify, Blueprint
import logging

health = Blueprint("health", __name__)


@health.route("/health", methods=["GET"])
def get_health():
    logging.info("Health check request")
    return jsonify(message="OK")
