# Contributing to AI_FOIS

## Development setup

1. Create a Python 3.11+ virtual environment.
2. Install dependencies with `pip install -r requirements.txt`.
3. Copy `.env.example` to `.env` and adjust local model settings.
4. Run `pytest` before opening a pull request.

Keep business logic in services, persistence in repositories, and Streamlit pages focused on presentation and input handling.

## Pull requests

Describe the operational problem, the change, and how it was tested. Do not commit PDFs, model files, vector databases, `.env` files, or generated logs.