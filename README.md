# Web Scraping Template

This project is a Python-based scraping template designed for web scraping tasks. It provides a structured framework with pre-configured modules for logging, caching, and making HTTP requests. The project is set up with modern Python tools and practices, making it a solid foundation for building robust web scrapers.

## Project Overview

### Key Technologies

*   **Programming Language:** Python 3.12+
*   **HTTP Clients:** `requests`, `httpx`
*   **Data Parsing:** `beautifulsoup4`
*   **Data Validation:** `pydantic`
*   **Dependency Management:** `uv` (inferred from `uv.lock`)
*   **Linting:** `ruff`
*   **Caching:** Redis
*   **Retry Logic:** `tenacity`

### Architecture

The project follows a modular structure:

*   `main.py`: The main entry point of the application.
*   `api/`: Contains the scraping logic, with classes that encapsulate interactions with specific websites.
*   `utils/`: Provides utility modules for common tasks like logging (`log.py`), making HTTP requests (`http_requests.py`), and caching (`redis_cache.py`).
*   `constants.py`: Stores constants and configuration variables.
*   `models.py`: Defines data models using `pydantic` for data validation and structuring.
*   `pyproject.toml`: Manages project dependencies and metadata.
*   `.github/workflows/`: Contains CI/CD workflows, such as the `ruff.yml` for linting.

## Getting Started

### 1. Setup

It is recommended to use `uv` for managing the virtual environment and dependencies.

**Create a virtual environment:**

```bash
python -m venv .venv
source .venv/bin/activate
```

**Install dependencies:**

```bash
uv pip sync pyproject.toml
```

**Set up environment variables:**

Copy the `sample.env` file to `.env` and fill in the required values.

```bash
cp sample.env .env
```

### 2. Running the Application

To run the main script:

```bash
python main.py
```

### 3. Running Tests

To run the test suite:

```bash
pytest
```

The test files are located in the `tests/` directory.

## Development Conventions

*   **Linting:** The project uses `ruff` for code linting. It is recommended to run `ruff check .` before committing changes. The CI pipeline will also run `ruff` on pull requests.
*   **Coding Style:** Follow the PEP 8 style guide. The `black` code formatter is included in the dependencies and can be used to format the code automatically.
*   **Type Hinting:** All new code should include type hints.
*   **Configuration:** Use the `.env` file for environment-specific configurations. Do not commit the `.env` file to version control.
*   **Logging:** Use the `get_logger` function from `utils.log` to get a logger instance for any new module.
*   **Error Handling:** Use the custom exceptions defined in `utils.exceptions` where appropriate.
*   **Dependency Management:** When adding new libraries using `uv add` or `uv install`, ensure you run `make requirements.txt` afterwards to update `requirements.txt`. This file is used for Docker builds and CI/CD pipelines, so keeping it up-to-date is crucial before pushing any changes.
