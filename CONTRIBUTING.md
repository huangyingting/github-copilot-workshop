# Contributing to GitHub Copilot Workshop

Thank you for your interest in contributing to the GitHub Copilot Workshop! This document provides guidelines and instructions for contributing to this project.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Getting Started](#getting-started)
- [Contribution Guidelines](#contribution-guidelines)
- [Style Guides](#style-guides)
- [Submitting Changes](#submitting-changes)

## Code of Conduct

This project adheres to a code of conduct that all contributors are expected to follow. By participating, you agree to:

- Be respectful and inclusive
- Welcome newcomers and help them learn
- Focus on constructive feedback
- Accept differing viewpoints gracefully
- Prioritize the community's best interests

## How Can I Contribute?

### Reporting Bugs

If you find a bug, please create an issue with:
- A clear, descriptive title
- Steps to reproduce the issue
- Expected vs. actual behavior
- Screenshots if applicable
- Your environment details (OS, IDE, Copilot version)

### Suggesting Enhancements

Enhancement suggestions are welcome! Please provide:
- A clear use case for the enhancement
- Why it would be useful to workshop participants
- Possible implementation approaches
- Examples from other resources (if applicable)

### Improving Documentation

Documentation improvements are always appreciated:
- Fix typos, grammar, or formatting issues
- Clarify confusing explanations
- Add missing information
- Improve code examples
- Update outdated content

### Adding New Content

You can contribute new content such as:
- New workshop modules or exercises
- Additional use cases and examples
- Custom instructions for specific technologies
- Reusable prompts for common tasks
- Custom chat modes for specialized workflows
- Tools and utilities to enhance the workshop

### Sharing Feedback

Share your experience with the workshop:
- What worked well for you
- What was confusing or unclear
- Suggestions for improvement
- Additional topics you'd like covered

## Getting Started

### Prerequisites

Before contributing, ensure you have:
- Git installed and configured
- GitHub account
- GitHub Copilot access (for testing Copilot-specific features)
- Python 3.11+ (for testing Python examples and tools)
- Basic understanding of Markdown

### Setting Up Your Development Environment

1. **Fork the repository** on GitHub

2. **Clone your fork locally**:
   ```bash
   git clone https://github.com/YOUR_USERNAME/github-copilot-workshop.git
   cd github-copilot-workshop
   ```

3. **Add the upstream repository**:
   ```bash
   git remote add upstream https://github.com/huangyingting/github-copilot-workshop.git
   ```

4. **Install dependencies** (for testing Python tools):
   ```bash
   pip install -r app/requirements.txt
   pip install -e .
   ```

5. **Create a branch** for your changes:
   ```bash
   git checkout -b feature/your-feature-name
   ```

## Contribution Guidelines

### Documentation Contributions

When contributing to documentation:

1. **Follow the existing structure**: Maintain the module-based organization
2. **Use clear headings**: Make content scannable with proper heading levels
3. **Include examples**: Add code snippets and command examples
4. **Add visuals**: Include screenshots, diagrams, or Mermaid charts when helpful
5. **Test all instructions**: Verify that all steps and examples work
6. **Keep it accessible**: Write for beginners while providing depth for advanced users

### Code Contributions

When contributing code examples or tools:

1. **Follow Python best practices**: Use PEP 8 style guide
2. **Add type hints**: Include type annotations for functions
3. **Write docstrings**: Document all public functions and classes
4. **Include comments**: Explain complex logic or Copilot-specific features
5. **Add error handling**: Handle edge cases gracefully
6. **Write tests**: Add unit tests for new functionality (if applicable)
7. **Keep it simple**: Prioritize readability over cleverness

### Custom Instructions and Prompts

When adding custom instructions, prompts, or chat modes:

1. **Focus on a specific domain**: Address a clear, well-defined use case
2. **Include metadata**: Add YAML frontmatter with description and mode
3. **Provide examples**: Show how to use the instruction/prompt
4. **Document tools needed**: Specify any required tools or dependencies
5. **Test thoroughly**: Verify it works as expected with Copilot
6. **Follow naming conventions**: Use descriptive, kebab-case filenames

### Exercise Contributions

When adding hands-on exercises:

1. **Define clear objectives**: State what participants will learn
2. **List prerequisites**: Specify required tools and knowledge
3. **Provide step-by-step instructions**: Make exercises easy to follow
4. **Include verification steps**: Help participants confirm success
5. **Add troubleshooting tips**: Address common issues
6. **Consider difficulty levels**: Label as beginner, intermediate, or advanced

## Style Guides

### Markdown Style

- Use ATX-style headers (`#` not underlines)
- Use fenced code blocks with language identifiers
- Use relative links for internal references
- Use reference-style links for external URLs
- One sentence per line for easier diffs
- Leave blank line before and after headings, lists, and code blocks

### Code Style

**Python**:
```python
def example_function(param1: str, param2: int = 0) -> dict:
    """
    Brief description of function.
    
    Args:
        param1: Description of param1
        param2: Description of param2
    
    Returns:
        Description of return value
    """
    result = {"key": "value"}
    return result
```

**Bash/Shell**:
```bash
#!/bin/bash
# Script description
set -euo pipefail

# Use long-form flags for readability
command --verbose --output file.txt
```

### Commit Message Style

Follow conventional commit format:

```
<type>[optional scope]: <description>

[optional body]

[optional footer]
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Formatting changes
- `refactor`: Code refactoring
- `test`: Adding tests
- `chore`: Maintenance tasks

Examples:
```
docs: add security review prompt template

feat(exercises): add Azure Functions migration exercise

fix: correct mermaid diagram rendering in slides

docs(readme): improve Module 5 code examples
```

## Submitting Changes

### Pull Request Process

1. **Ensure your changes are complete**:
   - All tests pass (if applicable)
   - Documentation is updated
   - Code is properly formatted
   - Commit messages are clear

2. **Update your branch** with the latest upstream changes:
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

3. **Push your changes**:
   ```bash
   git push origin feature/your-feature-name
   ```

4. **Create a Pull Request**:
   - Use a clear, descriptive title
   - Reference any related issues
   - Describe what changed and why
   - Include screenshots for UI changes
   - List any breaking changes

5. **Respond to feedback**:
   - Address reviewer comments promptly
   - Make requested changes
   - Ask questions if feedback is unclear
   - Be open to suggestions

### Pull Request Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Refactoring
- [ ] Other (please describe)

## Checklist
- [ ] I have followed the style guidelines
- [ ] I have performed a self-review
- [ ] I have commented complex code
- [ ] I have updated documentation
- [ ] My changes generate no new warnings
- [ ] I have tested my changes
- [ ] Screenshots included (if applicable)

## Related Issues
Closes #123

## Additional Context
Any additional information
```

## Review Process

After submitting a PR:

1. **Automated checks** will run (if configured)
2. **Maintainers will review** your contribution
3. **You may be asked to make changes**
4. **Once approved**, your PR will be merged

Review timeline:
- Initial response: Usually within 2-3 days
- Full review: Within 1 week for most PRs
- Complex changes may take longer

## Recognition

Contributors are recognized in several ways:
- Listed in repository contributors
- Mentioned in release notes (for significant contributions)
- Credited in documentation (for major additions)

## Questions?

If you have questions:
- Check existing [Issues](https://github.com/huangyingting/github-copilot-workshop/issues)
- Review [Discussions](https://github.com/huangyingting/github-copilot-workshop/discussions)
- Create a new issue with the `question` label

## License

By contributing, you agree that your contributions will be licensed under the same license as the project.

---

Thank you for contributing to the GitHub Copilot Workshop! Your efforts help make this resource better for everyone. 🚀
