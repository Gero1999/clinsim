# clinsim

A production-ready Python package scaffold for clinical simulation tooling.

## Features

- Modern `src/` layout
- PEP 621 metadata in `pyproject.toml`
- Testing with `pytest`
- Linting/formatting with `ruff`
- Static typing with `mypy`
- Pre-commit hooks
- GitHub Actions CI

## Project layout

```
clinsim/
├── .github/workflows/ci.yml
├── src/clinsim/
│   ├── __init__.py
│   ├── core.py
│   └── py.typed
├── tests/
│   └── test_core.py
├── pyproject.toml
├── .pre-commit-config.yaml
├── CONTRIBUTING.md
├── CHANGELOG.md
└── Makefile
```

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
```

Run checks:

```bash
make lint
make typecheck
make test
```

## Build package artifacts

```bash
make build
```

## Next steps

- Implement your domain logic in `src/clinsim/`
- Add more tests under `tests/`
- Update project metadata (authors, URLs, classifiers) in `pyproject.toml`