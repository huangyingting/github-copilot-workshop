"""
Simple Flask API Demo for GitHub Copilot Workshop.

This module demonstrates basic Flask API patterns and best practices
for use in GitHub Copilot demonstrations and exercises.
"""
from flask import Flask, jsonify, request
from typing import Dict, Any
import os

app = Flask(__name__)

# Configuration
app.config['DEBUG'] = os.getenv('FLASK_DEBUG', 'False') == 'True'
app.config['PORT'] = int(os.getenv('PORT', 5000))


@app.get("/")
def index() -> Dict[str, str]:
    """
    Root endpoint returning a welcome message.
    
    Returns:
        JSON response with welcome message
        
    Example:
        >>> response = requests.get('http://localhost:5000/')
        >>> print(response.json())
        {'message': 'Hello, World!', 'status': 'ok'}
    """
    return jsonify(message="Hello, World!", status="ok")


@app.get("/health")
def health() -> Dict[str, str]:
    """
    Health check endpoint for monitoring and load balancers.
    
    Returns:
        JSON response indicating service health status
        
    Example:
        >>> response = requests.get('http://localhost:5000/health')
        >>> print(response.json())
        {'status': 'healthy', 'service': 'copilot-workshop-api'}
    """
    return jsonify(status="healthy", service="copilot-workshop-api")


@app.get("/api/v1/info")
def api_info() -> Dict[str, Any]:
    """
    API information endpoint.
    
    Returns:
        JSON response with API metadata and available endpoints
        
    Example:
        >>> response = requests.get('http://localhost:5000/api/v1/info')
        >>> print(response.json()['version'])
        '1.0.0'
    """
    return jsonify(
        version="1.0.0",
        name="GitHub Copilot Workshop API",
        description="Demo API for GitHub Copilot workshop exercises",
        endpoints=[
            {"path": "/", "method": "GET", "description": "Welcome message"},
            {"path": "/health", "method": "GET", "description": "Health check"},
            {"path": "/api/v1/info", "method": "GET", "description": "API information"},
            {"path": "/api/v1/echo", "method": "POST", "description": "Echo request body"}
        ]
    )


@app.post("/api/v1/echo")
def echo() -> Dict[str, Any]:
    """
    Echo endpoint that returns the request body.
    
    Accepts JSON payload and returns it in the response.
    Useful for testing and demonstrating API requests.
    
    Returns:
        JSON response with the received data
        
    Example:
        >>> import requests
        >>> data = {'message': 'test'}
        >>> response = requests.post('http://localhost:5000/api/v1/echo', json=data)
        >>> print(response.json())
        {'received': {'message': 'test'}, 'status': 'echoed'}
    """
    data = request.get_json() or {}
    return jsonify(received=data, status="echoed")


@app.errorhandler(404)
def not_found(error) -> tuple[Dict[str, str], int]:
    """
    Handle 404 Not Found errors.
    
    Args:
        error: The error object
        
    Returns:
        JSON error response and 404 status code
    """
    return jsonify(error="Not Found", message="The requested resource does not exist"), 404


@app.errorhandler(500)
def internal_error(error) -> tuple[Dict[str, str], int]:
    """
    Handle 500 Internal Server Error.
    
    Args:
        error: The error object
        
    Returns:
        JSON error response and 500 status code
    """
    return jsonify(error="Internal Server Error", message="An unexpected error occurred"), 500


if __name__ == "__main__":
    port = app.config['PORT']
    debug = app.config['DEBUG']
    print(f"Starting GitHub Copilot Workshop API on port {port}")
    print(f"Debug mode: {debug}")
    print(f"Visit http://localhost:{port}/ to get started")
    app.run(host="0.0.0.0", port=port, debug=debug)
