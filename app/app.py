from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def index():
    return jsonify(message="Hello, World!")

@app.get("/skills")
def skills():
    return jsonify(skills=[
        {
            "name": "Code Completion",
            "description": "Real-time inline code suggestions as you type.",
        },
        {
            "name": "Code Chat",
            "description": "Ask questions about code and get explanations via Copilot Chat.",
        },
        {
            "name": "Code Refactoring",
            "description": "Refactor and improve code structure with AI-powered suggestions.",
        },
        {
            "name": "Test Generation",
            "description": "Automatically generate unit tests for your code.",
        },
        {
            "name": "Bug Fixing",
            "description": "Detect and fix bugs using /fix slash commands and inline suggestions.",
        },
        {
            "name": "Documentation",
            "description": "Generate docstrings, comments, and README content.",
        },
        {
            "name": "Agent Mode",
            "description": "Autonomous multi-step task execution across files and tools.",
        },
        {
            "name": "Custom Instructions",
            "description": "Define project-level guidelines to tailor Copilot responses.",
        },
        {
            "name": "Prompt Files",
            "description": "Reusable .prompt.md files for common coding tasks.",
        },
        {
            "name": "Custom Chat Modes",
            "description": "Custom chat modes that control tools and interaction style.",
        },
    ])

if __name__ == "__main__":
    app.run(debug=True)
