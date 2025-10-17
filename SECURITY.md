# Security Policy

## Supported Versions

This workshop repository is continuously updated. We recommend always using the latest version from the `main` branch.

| Version | Supported          |
| ------- | ------------------ |
| main    | :white_check_mark: |
| older   | :x:                |

## Reporting a Vulnerability

We take the security of our workshop materials seriously. If you discover a security vulnerability in any of the code examples, tools, or documentation, please report it responsibly.

### How to Report

**Please do NOT report security vulnerabilities through public GitHub issues.**

Instead, please report them via:

1. **GitHub Security Advisories** (Preferred):
   - Navigate to the repository's Security tab
   - Click "Report a vulnerability"
   - Fill in the details

2. **Direct Email**:
   - Contact the repository maintainer directly
   - Use a clear subject line: "Security Vulnerability in GitHub Copilot Workshop"
   - Include detailed information about the vulnerability

### What to Include

When reporting a vulnerability, please include:

1. **Type of vulnerability** (e.g., SQL injection, XSS, insecure configuration)
2. **Location** (file path and line numbers)
3. **Description** of the vulnerability
4. **Potential impact** if exploited
5. **Steps to reproduce** the vulnerability
6. **Suggested fix** (if you have one)
7. **Your contact information** for follow-up questions

### Example Report

```markdown
## Vulnerability Report

**Type**: SQL Injection
**Location**: `app/examples/database.py:45-50`
**Severity**: High

### Description
The database query uses string concatenation instead of parameterized queries,
making it vulnerable to SQL injection attacks.

### Current Code
```python
query = f"SELECT * FROM users WHERE username = '{username}'"
cursor.execute(query)
```

### Impact
An attacker could execute arbitrary SQL commands, potentially:
- Accessing sensitive user data
- Modifying or deleting database records
- Escalating privileges

### Reproduction Steps
1. Set username parameter to: `' OR '1'='1`
2. Execute the query
3. All user records are returned

### Suggested Fix
Use parameterized queries:
```python
query = "SELECT * FROM users WHERE username = ?"
cursor.execute(query, (username,))
```

### References
- [OWASP SQL Injection](https://owasp.org/www-community/attacks/SQL_Injection)
```

## Response Timeline

- **Initial Response**: Within 48 hours
- **Status Update**: Within 5 business days
- **Fix Timeline**: Depends on severity
  - Critical: 1-3 days
  - High: 1 week
  - Medium: 2 weeks
  - Low: Next regular update

## Disclosure Policy

- We follow a **coordinated disclosure** process
- Security vulnerabilities will be fixed before public disclosure
- We will credit reporters (unless they prefer to remain anonymous)
- A security advisory will be published after the fix is released

## Security Best Practices for Workshop Users

### When Using Workshop Examples

1. **Never use production credentials** in examples
2. **Review all code** before running it in your environment
3. **Update dependencies** to their latest secure versions
4. **Understand the code** before deploying to production
5. **Follow security best practices** outlined in the workshop

### For Code Examples

The workshop includes intentionally vulnerable code examples for educational purposes. These are clearly marked:

```python
# ⚠️ VULNERABLE CODE - FOR EDUCATIONAL PURPOSES ONLY
# This code demonstrates a SQL injection vulnerability
# DO NOT USE IN PRODUCTION
```

**Always check for these warnings before using code.**

### API Keys and Secrets

- **Never commit real API keys** to any repository
- Use **environment variables** for sensitive configuration
- Use **placeholder values** in examples (e.g., `YOUR_API_KEY`)
- Enable **GitHub secret scanning** on your own repositories

### Infrastructure Examples

Terraform and deployment examples in this workshop may include:

- Simplified security configurations for learning purposes
- Public access settings for demonstration
- Default credentials (clearly marked)

**Always harden security before production deployment:**

1. Enable encryption at rest and in transit
2. Implement proper network security groups
3. Use managed identities instead of API keys
4. Enable logging and monitoring
5. Follow principle of least privilege
6. Regular security audits

## Common Security Topics Covered

This workshop addresses security in several contexts:

### Module 3: Networking & Security
- Enterprise firewall considerations
- Proxy configuration security
- Traffic inspection techniques
- Allowlist management

### Module 4: Customization
- Secure handling of custom instructions
- Protecting sensitive data in prompts
- Safe use of extensions

### Module 10: Use Cases
- Secure script generation
- Infrastructure as Code security
- API security best practices
- Cloud resource security

## Security Resources

### GitHub Security Features
- [Secret Scanning](https://docs.github.com/en/code-security/secret-scanning)
- [Dependabot](https://docs.github.com/en/code-security/dependabot)
- [Code Scanning](https://docs.github.com/en/code-security/code-scanning)
- [Security Advisories](https://docs.github.com/en/code-security/security-advisories)

### External Resources
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [CWE/SANS Top 25](https://www.sans.org/top25-software-errors/)
- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)
- [Microsoft Security Development Lifecycle](https://www.microsoft.com/en-us/securityengineering/sdl/)

### Azure Security (for Azure-focused exercises)
- [Azure Security Baseline](https://docs.microsoft.com/en-us/security/benchmark/azure/)
- [Azure Security Best Practices](https://docs.microsoft.com/en-us/azure/security/fundamentals/best-practices-and-patterns)
- [Azure Well-Architected Framework - Security](https://docs.microsoft.com/en-us/azure/architecture/framework/security/)

## Dependency Security

This workshop uses minimal dependencies. For the Python tools:

```toml
[project]
dependencies = [
    "python-pptx>=1.0.2",
]
```

We regularly:
- Review dependencies for known vulnerabilities
- Update to latest stable versions
- Remove unused dependencies
- Use Dependabot for automated updates

## Workshop-Specific Security Notes

### Python Application (`app/`)
- Simple Flask example for demonstration
- Not intended for production use
- Shows basic patterns, not complete security implementation

### Tools (`tools/`)
- Utility scripts for workshop automation
- Designed for local use only
- Review code before running with elevated privileges

### Custom Instructions (`.github/`)
- Instructions may reference external services
- Always validate external integrations
- Review permissions granted to Copilot extensions

## Questions About Security?

If you have questions about security in this workshop:

1. Review the [Security documentation in Module 3](README.md#module-3-networking-security-and-data-flow-enterprise)
2. Check existing [Security-related issues](https://github.com/huangyingting/github-copilot-workshop/labels/security)
3. Create a public issue for general security questions (not vulnerabilities)
4. Contact maintainers directly for sensitive matters

## Acknowledgments

We appreciate the security research community's efforts to keep this workshop safe and educational. Security researchers who responsibly disclose vulnerabilities will be acknowledged (unless they prefer anonymity).

---

**Remember**: This workshop is educational. Always apply proper security practices when adapting examples to production environments.
