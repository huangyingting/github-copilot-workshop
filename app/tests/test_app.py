"""
Unit tests for the GitHub Copilot Workshop Flask API.

Run with: pytest tests/test_app.py -v
"""
import pytest
from app import app as flask_app


@pytest.fixture
def app():
    """Create and configure a test Flask application."""
    flask_app.config['TESTING'] = True
    return flask_app


@pytest.fixture
def client(app):
    """Create a test client for the Flask application."""
    return app.test_client()


class TestRootEndpoint:
    """Test suite for the root endpoint."""
    
    def test_index_returns_200(self, client):
        """Test that root endpoint returns 200 OK."""
        response = client.get('/')
        assert response.status_code == 200
    
    def test_index_returns_json(self, client):
        """Test that root endpoint returns JSON content."""
        response = client.get('/')
        assert response.content_type == 'application/json'
    
    def test_index_message_content(self, client):
        """Test that root endpoint returns expected message."""
        response = client.get('/')
        data = response.get_json()
        assert data['message'] == 'Hello, World!'
        assert data['status'] == 'ok'


class TestHealthEndpoint:
    """Test suite for the health check endpoint."""
    
    def test_health_returns_200(self, client):
        """Test that health endpoint returns 200 OK."""
        response = client.get('/health')
        assert response.status_code == 200
    
    def test_health_status(self, client):
        """Test that health endpoint returns healthy status."""
        response = client.get('/health')
        data = response.get_json()
        assert data['status'] == 'healthy'
        assert data['service'] == 'copilot-workshop-api'


class TestAPIInfoEndpoint:
    """Test suite for the API information endpoint."""
    
    def test_info_returns_200(self, client):
        """Test that info endpoint returns 200 OK."""
        response = client.get('/api/v1/info')
        assert response.status_code == 200
    
    def test_info_has_version(self, client):
        """Test that info endpoint includes version information."""
        response = client.get('/api/v1/info')
        data = response.get_json()
        assert 'version' in data
        assert data['version'] == '1.0.0'
    
    def test_info_has_endpoints(self, client):
        """Test that info endpoint lists available endpoints."""
        response = client.get('/api/v1/info')
        data = response.get_json()
        assert 'endpoints' in data
        assert isinstance(data['endpoints'], list)
        assert len(data['endpoints']) > 0


class TestEchoEndpoint:
    """Test suite for the echo endpoint."""
    
    def test_echo_returns_200(self, client):
        """Test that echo endpoint returns 200 OK."""
        response = client.post('/api/v1/echo', json={'test': 'data'})
        assert response.status_code == 200
    
    def test_echo_returns_received_data(self, client):
        """Test that echo endpoint returns the sent data."""
        test_data = {'message': 'Hello', 'number': 42}
        response = client.post('/api/v1/echo', json=test_data)
        data = response.get_json()
        assert data['received'] == test_data
        assert data['status'] == 'echoed'
    
    def test_echo_handles_empty_body(self, client):
        """Test that echo endpoint handles empty request body."""
        response = client.post('/api/v1/echo')
        assert response.status_code == 200
        data = response.get_json()
        assert data['received'] == {}
    
    def test_echo_with_nested_data(self, client):
        """Test that echo endpoint handles nested JSON data."""
        test_data = {
            'user': {
                'name': 'John',
                'age': 30
            },
            'items': [1, 2, 3]
        }
        response = client.post('/api/v1/echo', json=test_data)
        data = response.get_json()
        assert data['received'] == test_data


class TestErrorHandlers:
    """Test suite for error handling."""
    
    def test_404_not_found(self, client):
        """Test that invalid routes return 404 Not Found."""
        response = client.get('/nonexistent')
        assert response.status_code == 404
    
    def test_404_returns_json(self, client):
        """Test that 404 errors return JSON response."""
        response = client.get('/nonexistent')
        assert response.content_type == 'application/json'
        data = response.get_json()
        assert 'error' in data
        assert data['error'] == 'Not Found'


class TestHTTPMethods:
    """Test suite for HTTP method handling."""
    
    def test_post_to_get_endpoint_fails(self, client):
        """Test that POST to GET-only endpoint returns 405."""
        response = client.post('/')
        assert response.status_code == 405
    
    def test_get_to_post_endpoint_fails(self, client):
        """Test that GET to POST-only endpoint returns 405."""
        response = client.get('/api/v1/echo')
        assert response.status_code == 405


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
