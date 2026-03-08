# Contributing

## Setup

1. Create and activate a virtual environment.
2. Install in editable mode with development extras:

```bash
pip install -e .[dev]
```

3. Install pre-commit hooks:

```bash
pre-commit install
```

## Development Commands

- Run linting: `ruff check .`
- Run formatting: `ruff format .`
- Run type checks: `mypy src`
- Run tests: `pytest`

## Pull Requests

- Keep changes focused and small.
- Ensure CI passes before requesting review.
