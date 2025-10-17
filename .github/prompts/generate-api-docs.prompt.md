---
description: "Generate API documentation from code with examples"
mode: 'agent'
---

# Generate API Documentation

Create comprehensive API documentation for the selected code, including endpoints, request/response formats, and examples.

## Documentation Structure

### For REST APIs

```markdown
## Endpoint Name

**URL**: `/api/v1/resource`
**Method**: `GET | POST | PUT | DELETE`
**Auth Required**: Yes/No

### Description
Brief description of what this endpoint does.

### Request Headers
| Header | Type | Required | Description |
|--------|------|----------|-------------|
| Authorization | string | Yes | Bearer token |
| Content-Type | string | Yes | application/json |

### Request Parameters
| Parameter | Type | Required | Description | Example |
|-----------|------|----------|-------------|---------|
| id | integer | Yes | Resource ID | 123 |
| name | string | No | Resource name | "example" |

### Request Body (if applicable)
```json
{
  "field1": "value1",
  "field2": 123
}
```

### Success Response
**Code**: 200 OK
**Content**:
```json
{
  "id": 123,
  "name": "example",
  "created_at": "2025-01-01T00:00:00Z"
}
```

### Error Responses
**Code**: 400 Bad Request
**Content**:
```json
{
  "error": "Invalid input",
  "details": "field1 is required"
}
```

**Code**: 401 Unauthorized
**Content**:
```json
{
  "error": "Authentication required"
}
```

### Example Usage

**cURL**:
```bash
curl -X GET "https://api.example.com/api/v1/resource/123" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

**Python**:
```python
import requests

response = requests.get(
    "https://api.example.com/api/v1/resource/123",
    headers={"Authorization": "Bearer YOUR_TOKEN"}
)
data = response.json()
```

**JavaScript**:
```javascript
fetch('https://api.example.com/api/v1/resource/123', {
  headers: { 'Authorization': 'Bearer YOUR_TOKEN' }
})
  .then(res => res.json())
  .then(data => console.log(data));
```
```

### For Python Functions/Methods

```python
def function_name(param1: str, param2: int = 0) -> dict:
    """
    Brief description of what the function does.
    
    This function performs X operation and returns Y result.
    It handles Z edge cases by doing A.
    
    Args:
        param1 (str): Description of param1. Example: "value"
        param2 (int, optional): Description of param2. Defaults to 0.
    
    Returns:
        dict: Description of return value structure
            {
                'key1': 'value1',
                'key2': 123
            }
    
    Raises:
        ValueError: If param1 is empty
        TypeError: If param2 is not an integer
    
    Examples:
        Basic usage:
        >>> result = function_name("test", 5)
        >>> print(result)
        {'key1': 'value1', 'key2': 123}
        
        With default parameter:
        >>> result = function_name("test")
        >>> print(result)
        {'key1': 'value1', 'key2': 0}
    
    Notes:
        - Important consideration 1
        - Important consideration 2
    
    See Also:
        - related_function(): Description of relationship
    """
    pass
```

## Documentation Requirements

1. **Completeness**: Document all public endpoints/functions
2. **Clarity**: Use simple, clear language
3. **Examples**: Provide working code examples
4. **Error Handling**: Document all error cases
5. **Types**: Include type information
6. **Versioning**: Indicate API version if applicable
7. **Authentication**: Clearly state auth requirements
8. **Rate Limits**: Document any rate limiting
9. **Deprecation**: Note deprecated features
10. **Updates**: Include last updated date

## Usage

1. Select the API code (routes, handlers, or functions)
2. Run: `Ctrl+/` → `generate-api-docs`
3. Review and customize generated documentation
4. Add to `docs/api.md` or inline docstrings
5. Keep documentation in sync with code changes
