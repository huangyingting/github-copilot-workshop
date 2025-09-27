"""
Flask application for the GitHub Copilot Workshop.

This is a simple demo application showing basic Flask structure
with proper error handling and best practices.
"""

from flask import Flask, jsonify
import logging
import os

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Configuration
app.config['JSON_SORT_KEYS'] = False


@app.route("/")
def index():
    """
    Home endpoint that returns a welcome message.
    
    Returns:
        JSON response with a welcome message
    """
    try:
        return jsonify({
            "message": "Hello, World!",
            "status": "success",
            "service": "GitHub Copilot Workshop API"
        })
    except Exception as e:
        logger.error(f"Error in index route: {e}")
        return jsonify({
            "message": "Internal server error",
            "status": "error"
        }), 500


@app.route("/health")
def health_check():
    """
    Health check endpoint for monitoring.
    
    Returns:
        JSON response with health status
    """
    return jsonify({
        "status": "healthy",
        "service": "GitHub Copilot Workshop API"
    })


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({
        "message": "Resource not found",
        "status": "error"
    }), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    return jsonify({
        "message": "Internal server error",
        "status": "error"
    }), 500


if __name__ == "__main__":
    # Get configuration from environment variables
    debug_mode = os.getenv("FLASK_DEBUG", "False").lower() == "true"
    port = int(os.getenv("PORT", 5000))
    host = os.getenv("HOST", "127.0.0.1")
    
    logger.info(f"Starting Flask app on {host}:{port} (debug={debug_mode})")
    app.run(host=host, port=port, debug=debug_mode)
