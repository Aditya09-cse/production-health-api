from flask import Flask, jsonify
from routes.notes import notes_bp

from utils.logger import setup_logger
from routes.health import health_bp

logger = setup_logger()

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(health_bp)
app.register_blueprint(notes_bp)

logger.info("Application Started")


@app.route("/")
def home():
    logger.info("Home endpoint accessed")

    return jsonify({
        "message": "Production Health API",
        "status": "running",
        "documentation": "/health"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)