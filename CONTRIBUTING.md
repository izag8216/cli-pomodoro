# Contributing

Contributions are welcome! Please follow these guidelines:

## Development Setup

1. Clone the repository
2. Create a virtual environment: `python -m venv .venv && source .venv/bin/activate`
3. Install dev dependencies: `pip install -e ".[dev]"`
4. Run tests: `pytest`

## Code Style

- Follow PEP 8
- Use type hints
- Maximum line length: 100

## Commit Convention

Use conventional commits:
- `feat:` for new features
- `fix:` for bug fixes
- `docs:` for documentation
- `test:` for tests
- `refactor:` for refactoring

## Pull Requests

1. Ensure all tests pass
2. Run linting: `ruff check src/ tests/`
3. Add tests for new features
4. Update documentation as needed
