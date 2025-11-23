---
description: "Review code for security vulnerabilities and best practices"
mode: 'agent'
tools: ['codebase', 'search', 'githubRepo']
---

# Security Code Review

Perform a comprehensive security review of the selected code or file.

## Review Checklist

### Input Validation
- [ ] All user inputs are validated and sanitized
- [ ] Type checking is performed on inputs
- [ ] Length/size limits are enforced
- [ ] Special characters are properly escaped

### Authentication & Authorization
- [ ] Authentication mechanisms are secure
- [ ] Authorization checks are present
- [ ] Session management is secure
- [ ] Password handling follows best practices

### Data Protection
- [ ] Sensitive data is encrypted at rest
- [ ] Sensitive data is encrypted in transit
- [ ] No hardcoded secrets or credentials
- [ ] Environment variables used for configuration

### SQL & Injection Prevention
- [ ] Parameterized queries are used (no string concatenation)
- [ ] ORM frameworks used properly
- [ ] Input sanitization prevents SQL injection
- [ ] NoSQL injection prevention (if applicable)

### API Security
- [ ] Rate limiting is implemented
- [ ] CORS is properly configured
- [ ] API authentication is required
- [ ] API responses don't leak sensitive info

### Error Handling
- [ ] Errors don't expose sensitive information
- [ ] Stack traces not shown to users
- [ ] Proper logging without sensitive data
- [ ] Graceful degradation on errors

### Dependencies
- [ ] No known vulnerable dependencies
- [ ] Dependencies are up to date
- [ ] Minimal dependencies used
- [ ] Supply chain security considered

### Code Quality
- [ ] No commented-out sensitive code
- [ ] Secure coding practices followed
- [ ] Principle of least privilege applied
- [ ] Defense in depth implemented

## Report Format

For each issue found, provide:
1. **Severity**: Critical / High / Medium / Low
2. **Category**: (e.g., Input Validation, SQL Injection, etc.)
3. **Location**: File and line number
4. **Description**: What the issue is
5. **Risk**: What could happen
6. **Recommendation**: How to fix it
7. **Code Example**: Show the fix

## Example Output

```markdown
### Issue 1: SQL Injection Vulnerability
**Severity**: Critical
**Location**: `app.py:45`
**Description**: User input directly concatenated into SQL query
**Risk**: Attacker could execute arbitrary SQL commands
**Recommendation**: Use parameterized queries

**Current Code**:
```python
query = f"SELECT * FROM users WHERE username = '{username}'"
```

**Fixed Code**:
```python
query = "SELECT * FROM users WHERE username = ?"
cursor.execute(query, (username,))
```
```

## Usage

1. Select the code file or section to review
2. Run this prompt: `Ctrl+/` → `security-review`
3. Review findings and prioritize fixes
4. Implement recommendations
5. Re-run review to verify fixes
