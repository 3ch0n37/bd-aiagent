
# BD-AIAgent

An AI-powered coding assistant that can perform various file operations and help with code-related tasks.
This project is part of the course on [boot.dev](https://www.boot.dev).

## Description

BD-AIAgent is a command-line tool that leverages Google's Gemini AI to provide intelligent coding assistance.
The agent can:

- List files and directories
- Read file contents
- Execute Python files with arguments
- Write or modify files

## Requirements

- Python >= 3.13
- Google Gemini API key
- Dependencies are managed using `uv` package manager

## Installation

1. Clone the repository
2. Install dependencies:

```sh
uv install
```

3. Create a `.env` file in the project root and add your Gemini API key:

```
GEMINI_API_KEY=your_api_key_here
```


## Usage

Run the AI agent with your prompt:

```sh
python main.py "Your prompt here" [--verbose]
```


### Examples

```sh
# List project files
python main.py "Show me all files in the project"
# Read a specific file
python main.py "Show me the content of main.py"
# Execute a Python file
python main.py "Run the tests"
# Get help with code
python main.py "How do I fix this error?"
```


Use the `--verbose` flag for detailed output including token counts and function call details.

## Security Note

The agent is designed to operate only within the project directory for security. It will refuse to access files outside
this boundary.
