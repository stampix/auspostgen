.PHONY: install setup test lint format clean

# Install dependencies
install:
	poetry install

# Setup development environment
setup: install
	poetry run pre-commit install

# Run tests
test:
	poetry run pytest

# Run all linters
lint:
	poetry run black --check .
	poetry run isort --check .
	poetry run mypy .
	poetry run ruff check .

# Format code
format:
	poetry run black .
	poetry run isort .
	poetry run ruff check --fix .

# Clean up
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.pyd" -delete
	find . -type f -name ".coverage" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type d -name "*.egg" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +
	find . -type d -name ".ruff_cache" -exec rm -rf {} +
