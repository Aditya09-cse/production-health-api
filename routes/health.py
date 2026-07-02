from flask import Blueprint, jsonify
from config import Config
from utils.system import get_system_metrics

health_bp = Blueprint("health", __name__)


@health_bp.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "healthy",
        "application": Config.APP_NAME,
        "version": Config.VERSION
    })


@health_bp.route("/version", methods=["GET"])
def version():
    return jsonify({
        "application": Config.APP_NAME,
        "version": Config.VERSION
    })


@health_bp.route("/metrics", methods=["GET"])
def metrics():
    return jsonify(get_system_metrics())