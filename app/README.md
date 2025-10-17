# GitHub Copilot Workshop - Sample Flask Application

This is a simple Flask API application used for demonstrations and exercises in the GitHub Copilot workshop.

## Purpose

This application serves as:
- A reference implementation for Flask API development
- A demo for using GitHub Copilot with Python and Flask
- A starting point for workshop exercises
- An example of well-documented, type-annotated Python code

## Features

- **RESTful API endpoints** with proper HTTP methods
- **JSON responses** for all endpoints
- **Error handling** with custom error handlers
- **Health check endpoint** for monitoring
- **API information endpoint** for documentation
- **Echo endpoint** for testing requests
- **Type annotations** for better IDE support
- **Comprehensive docstrings** following Google style
- **Environment-based configuration**

## Installation

### Prerequisites

- Python 3.11 or higher
- pip or uv package manager

### Setup

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

   Or using uv:
   ```bash
   uv pip install -r requirements.txt
   ```

2. **Set environment variables** (optional):
   ```bash
   export FLASK_DEBUG=True
   export PORT=5000
   ```

## Running the Application

### Development Mode

```bash
python app.py
```

Or with Flask CLI:
```bash
flask --app app run --debug
```

### Production Mode

For production, use a WSGI server like Gunicorn:

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## API Endpoints

### Root Endpoint
- **URL**: `/`
- **Method**: `GET`
- **Description**: Returns a welcome message
- **Response**:
  ```json
  {
    "message": "Hello, World!",
    "status": "ok"
  }
  ```

### Health Check
- **URL**: `/health`
- **Method**: `GET`
- **Description**: Health check for monitoring
- **Response**:
  ```json
  {
    "status": "healthy",
    "service": "copilot-workshop-api"
  }
  ```

### API Information
- **URL**: `/api/v1/info`
- **Method**: `GET`
- **Description**: Returns API metadata and available endpoints
- **Response**:
  ```json
  {
    "version": "1.0.0",
    "name": "GitHub Copilot Workshop API",
    "description": "Demo API for GitHub Copilot workshop exercises",
    "endpoints": [...]
  }
  ```

### Echo Endpoint
- **URL**: `/api/v1/echo`
- **Method**: `POST`
- **Description**: Echoes back the request body
- **Request Body**: Any valid JSON
- **Response**:
  ```json
  {
    "received": { ... },
    "status": "echoed"
  }
  ```

## Testing

### Manual Testing with cURL

```bash
# Test root endpoint
curl http://localhost:5000/

# Test health check
curl http://localhost:5000/health

# Test API info
curl http://localhost:5000/api/v1/info

# Test echo endpoint
curl -X POST http://localhost:5000/api/v1/echo \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello from cURL"}'
```

### Manual Testing with Python

```python
import requests

base_url = "http://localhost:5000"

# Test root endpoint
response = requests.get(f"{base_url}/")
print(response.json())

# Test echo endpoint
data = {"message": "Hello from Python"}
response = requests.post(f"{base_url}/api/v1/echo", json=data)
print(response.json())
```

### Automated Testing

Run tests with pytest:
```bash
pytest tests/test_app.py -v
```

## Using with GitHub Copilot

This application is designed to demonstrate GitHub Copilot capabilities:

### Code Completion
1. Open `app.py` in your IDE
2. Try adding a new endpoint by typing a comment:
   ```python
   # Add a new endpoint for user greeting with name parameter
   ```
3. Watch Copilot suggest the implementation

### Code Generation
Ask Copilot Chat:
- "Add input validation to the echo endpoint"
- "Create a middleware for request logging"
- "Add rate limiting to the API"
- "Generate unit tests for all endpoints"

### Refactoring
Select code and ask Copilot:
- "Refactor this to use blueprints"
- "Add async/await support"
- "Improve error handling"
- "Add request validation with marshmallow"

### Documentation
Ask Copilot Chat:
- "Generate OpenAPI/Swagger documentation for this API"
- "Create a Postman collection for these endpoints"
- "Write integration tests for the API"

## Workshop Exercises

### Exercise 1: Add a New Endpoint
**Objective**: Practice using Copilot for code generation

1. Add a `/api/v1/status` endpoint that returns server statistics
2. Include: timestamp, uptime, request count
3. Use Copilot to generate the implementation

### Exercise 2: Add Input Validation
**Objective**: Enhance API robustness

1. Add validation to the echo endpoint
2. Require specific fields in the request body
3. Return appropriate error messages
4. Use Copilot to suggest validation patterns

### Exercise 3: Add Authentication
**Objective**: Implement security features

1. Add API key authentication
2. Protect all `/api/v1/*` endpoints
3. Add an `/auth/login` endpoint
4. Use Copilot to implement JWT tokens

### Exercise 4: Add Database Integration
**Objective**: Work with data persistence

1. Add SQLite database support
2. Create a simple User model
3. Add CRUD endpoints for users
4. Use Copilot to generate database operations

## Docker Support

### Build Image
```bash
docker build -t copilot-workshop-api .
```

### Run Container
```bash
docker run -p 5000:5000 copilot-workshop-api
```

### Docker Compose
```bash
docker-compose up
```

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `FLASK_DEBUG` | Enable debug mode | `False` |
| `PORT` | Server port | `5000` |

## Project Structure

```
app/
├── app.py              # Main application file
├── requirements.txt    # Python dependencies
├── README.md          # This file
└── tests/             # Test files (optional)
    └── test_app.py    # Unit tests
```

## Best Practices Demonstrated

1. **Type Hints**: All functions use type annotations
2. **Docstrings**: Comprehensive documentation for all endpoints
3. **Error Handling**: Custom error handlers for common HTTP errors
4. **Configuration**: Environment-based configuration
5. **REST Conventions**: Proper use of HTTP methods and status codes
6. **JSON Responses**: Consistent JSON structure
7. **Health Checks**: Standard health check endpoint
8. **API Versioning**: Version prefix in URLs (`/api/v1/`)

## Common Issues

### Port Already in Use
```bash
# Find process using port 5000
lsof -i :5000

# Kill the process
kill -9 <PID>

# Or use a different port
export PORT=8080
python app.py
```

### Import Errors
```bash
# Make sure you're in the app directory
cd app

# Install dependencies
pip install -r requirements.txt
```

## Next Steps

1. Explore the code with GitHub Copilot
2. Try the workshop exercises
3. Add your own endpoints
4. Experiment with Copilot Chat for refactoring
5. Use custom prompts to enhance the application

## Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Flask REST API Tutorial](https://flask.palletsprojects.com/en/latest/tutorial/)
- [Python Type Hints](https://docs.python.org/3/library/typing.html)
- [REST API Best Practices](https://restfulapi.net/)

---

**Note**: This is a demo application for educational purposes. For production use, implement proper security, authentication, database integration, and error handling.
