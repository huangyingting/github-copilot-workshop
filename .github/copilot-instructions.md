# GitHub Copilot Workshop - Repository Instructions

## Repository Context

This repository is a comprehensive workshop for learning GitHub Copilot capabilities, features, and best practices. It contains documentation, code examples, tools, and hands-on exercises designed to help developers maximize their productivity with GitHub Copilot.

## Code Generation Guidelines

### Documentation Standards
- Use clear, concise language suitable for technical workshops
- Include code examples with inline comments explaining key concepts
- Follow Markdown best practices for formatting
- Add diagrams using Mermaid.js for complex workflows
- Include speaker notes for presentation-ready content

### Python Code Standards
- Follow PEP 8 style guidelines
- Use type hints for function parameters and return values
- Include docstrings for all functions, classes, and modules
- Use meaningful variable and function names
- Add inline comments for complex logic
- Prefer explicit over implicit code

### Workshop Exercise Standards
- Structure exercises with clear objectives and prerequisites
- Include step-by-step instructions with expected outcomes
- Provide sample code snippets and prompts
- Add troubleshooting tips for common issues
- Include verification steps to confirm success

### Tool Development Standards
- Create reusable, well-documented utility scripts
- Handle errors gracefully with informative messages
- Support command-line arguments with help text
- Include usage examples in docstrings
- Write modular, testable code

## File Organization

### `.github/` Directory Structure
- `instructions/*.instructions.md` - Domain-specific custom instructions (e.g., Kubernetes, Azure)
- `prompts/*.prompt.md` - Reusable prompt templates for common tasks
- `chatmodes/*.chatmode.md` - Custom chat modes for specialized workflows
- `ISSUE_TEMPLATE/` - Issue templates for bugs, features, and documentation

### Key Files
- `README.md` - Main workshop documentation with all modules
- `slides/README-slides.md` - Presentation-ready version of documentation
- `app/` - Sample applications for demonstrations
- `tools/` - Utility scripts for automation
- `images/` - Screenshots and diagrams

## Custom Instructions Usage

### When Creating New Custom Instructions
- Focus on a specific domain or technology
- Include core concepts and best practices
- Provide examples of common patterns
- Add troubleshooting guidelines
- Reference official documentation

### When Creating New Prompts
- Define clear, specific objectives
- Include context about when to use the prompt
- Specify required inputs and expected outputs
- Add examples of successful usage
- Keep prompts reusable across projects

### When Creating New Chat Modes
- Define the mode's purpose and scope
- Specify which tools should be available
- Set clear boundaries for the mode's behavior
- Include examples of appropriate use cases
- Document any limitations

## Best Practices for This Repository

1. **Keep Examples Current**: Update code examples to use latest features and APIs
2. **Maintain Consistency**: Follow established patterns for documentation and code
3. **Add Context**: Include real-world scenarios and use cases
4. **Test Thoroughly**: Verify all code examples and exercises work as documented
5. **Document Changes**: Update relevant sections when adding new features
6. **Consider Audience**: Write for developers new to GitHub Copilot
7. **Show Progressive Complexity**: Start simple, build to advanced topics
8. **Include Visuals**: Add screenshots, diagrams, and code snippets liberally

## Copilot-Specific Conventions

### For Code Suggestions
- Generate complete, working examples
- Include error handling and edge cases
- Add comments explaining Copilot-specific features
- Show multiple approaches when applicable

### For Chat Responses
- Reference workshop modules when relevant
- Suggest related exercises or examples
- Link to official documentation
- Provide context about why an approach is recommended

### For Documentation
- Use active voice and clear headings
- Include command examples with expected output
- Add links to related sections
- Provide visual aids for complex concepts

## Security and Privacy

- Never include real API keys, secrets, or credentials in examples
- Use placeholder values (e.g., `YOUR_API_KEY`, `<unique_string>`)
- Remind users to secure sensitive information
- Follow GitHub security best practices
- Include security considerations in architecture examples

## Contribution Guidelines

When suggesting improvements or additions:
- Align with existing workshop structure
- Maintain consistent formatting and style
- Add examples that complement existing content
- Update relevant indexes and navigation
- Consider workshop flow and learning progression
- Test all code examples before adding them
- Include attribution for external resources
