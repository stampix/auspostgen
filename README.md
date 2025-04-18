# AusPostGen

A Python library for generating Australia Post Barcode versions 37, 59, and 62.

This is a fork off the auspostgen project by damiandennis maintained by Stampix.
The goal of this fork was to make the package more modern and be usable in newer projects.

## Features

- Generate Australia Post barcodes in various formats
- Support for versions 37, 59, and 62
- High-performance C extension for barcode generation
- Simple Python API

## Installation

```bash
# Using Poetry
poetry add stampix-auspostgen

# Using pip
pip install stampix-auspostgen
```

## Usage

```python
from stampix.auspostgen.generator import write_image

# Generate a barcode image
write_image("output.png", "12345678901234567890", version=37)
```

## Development

1. Clone the repository
2. Install dependencies:
   ```bash
   poetry install
   ```
3. Run tests:
   ```bash
   poetry run pytest
   ```

### Notes

- There are some file comparison tests in the repo, but they don't give exactly the same results cross-platform so leaving this as is for now.

- python-semantic-release doesn't update the version number inside the toml file & `__init__.py` for some reason. We will take a look later.

## Project Structure

```
auspostgen/
├── stampix/
│   ├── __init__.py
│   └── auspostgen/
│       └── _c/
│           ├── __init__.py
│           ├── auspost.c
│           └── Makefile
├── tests/
│   └── __init__.py
├── docs/
├── pyproject.toml
└── README.md
```

## License

MIT License - see LICENSE.txt for details
