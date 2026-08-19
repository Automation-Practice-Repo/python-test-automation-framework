# Enterprise Python Test Automation Framework

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Pytest](https://img.shields.io/badge/Pytest-8.0%2B-green.svg)](https://docs.pytest.org/)
[![Playwright](https://img.shields.io/badge/Playwright-1.40%2B-red.svg)](https://playwright.dev/python/)
[![MongoDB](https://img.shields.io/badge/MongoDB-Atlas-green.svg)](https://www.mongodb.com/)
[![SQL](https://img.shields.io/badge/SQL-PostgreSQL%2FGeneric-blue.svg)](https://www.postgresql.org/)
[![Allure Reports](https://img.shields.io/badge/Allure-Reporting-orange.svg)](https://docs.qameta.io/allure/)
[![GitHub Actions](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-black.svg)](https://github.com/features/actions)

## Project Overview

This repository contains a modern, production-grade, portfolio-ready Python Test Automation Framework. Designed for scalability, maintainability, and enterprise QA practices, it integrates UI, API, and backend database integrity testing into a unified execution pipeline.

Key Capabilities:
- **UI Automation**: Playwright for Python using Page Object Model (POM) and robust element selection strategy (role, text, test-id).
- **API Testing**: HTTP client abstraction using `requests` with automatic header management, environment-based credentials, and status/schema validation.
- **Backend Database Integrity Validation**: Multi-database support with SQL query execution (PostgreSQL/SQLAlchemy compatible) and MongoDB Atlas document validation.
- **Data-Driven Testing**: Pytest parametrization, JSON test data support, and environment-driven configuration using `python-dotenv`.
- **Reporting**: Allure Reports integration with rich step execution details and screenshot/artifact attachments.
- **CI/CD Execution**: GitHub Actions integration for automated regression, scheduled nightly execution, and artifact retention.

### End-to-End Validation Strategy
```
UI/API Action  --->  Database Update (SQL / MongoDB)  --->  Backend Query Validation  --->  Pytest Assertion / Allure Report
```

---

## Tech Stack

- **Language**: Python 3.10+
- **Test Runner**: Pytest 8.0+
- **Browser Automation**: Playwright Python
- **API Testing**: Requests / HTTPX
- **SQL Tooling**: Psycopg2-binary / SQLAlchemy
- **NoSQL Database**: PyMongo (MongoDB Atlas)
- **Reporting**: Allure Pytest
- **CI/CD**: GitHub Actions

---

## Project Structure

```text
python-test-automation-framework/
├── .github/
│   └── workflows/
│       └── test_runner.yml
├── api_tests/
│   ├── __init__.py
│   └── test_health_api.py
├── config/
│   ├── __init__.py
│   └── settings.py
├── db_queries/
│   ├── __init__.py
│   ├── mongodb_queries.py
│   └── sql_queries.py
├── fixtures/
│   ├── __init__.py
│   └── db_fixtures.py
├── locators/
│   ├── __init__.py
│   └── home_locators.py
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   └── home_page.py
├── test_data/
│   ├── __init__.py
│   └── sample_data.json
├── ui_tests/
│   ├── __init__.py
│   └── test_home_ui.py
├── utils/
│   ├── __init__.py
│   ├── api_client.py
│   ├── mongo_client.py
│   └── sql_client.py
├── .env.example
├── .gitignore
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

### Key Directory Explanations
- `ui_tests/`: Pytest suite containing end-to-end UI tests.
- `api_tests/`: Pytest suite containing REST API tests.
- `pages/`: Page Object Model (POM) classes encapsulating page actions.
- `locators/`: Centralized locator definitions separating selectors from page behavior.
- `utils/`: Reusable wrappers for HTTP API client, SQL queries, and MongoDB client.
- `db_queries/`: Specific SQL queries and MongoDB document lookup helper methods.
- `fixtures/`: Pytest shared fixtures for database connections and queries.
- `config/`: Environment configuration manager loading `.env` variables safely.
- `test_data/`: Static JSON/CSV test data used in data-driven test scenarios.

---

## Prerequisites

- **Python**: 3.10 or higher installed
- **Node.js / npx**: Required for installing Playwright browser binaries
- **Allure Commandline**: (Optional for local viewing) `brew install allure` (macOS) or `scoop install allure` (Windows)

---

## Local Setup & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/python-test-automation-framework.git
cd python-test-automation-framework
```

### 2. Create Virtual Environment
- **macOS / Linux**:
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```
- **Windows (PowerShell)**:
  ```powershell
  python -m venv venv
  .\venv\Scripts\Activate.ps1
  ```
- **Windows (Command Prompt)**:
  ```cmd
  python -m venv venv
  .\venv\Scripts\activate.bat
  ```

### 3. Install Dependencies & Playwright Browsers
```bash
pip install --upgrade pip
pip install -r requirements.txt
playwright install
```

### 4. Configure Environment Variables
Copy `.env.example` to `.env`:
```bash
cp .env.example .env
```
Edit `.env` to configure your target base URL, API keys, SQL credentials, and MongoDB connection string.

---

## Environment Variables

| Variable | Description | Default Value / Example |
|---|---|---|
| `BASE_URL` | Target web app URL | `https://freshlife.in` |
| `ENVIRONMENT` | Target environment mode | `qa` / `staging` / `prod` |
| `API_BASE_URL` | REST API base URL | `https://freshlife.in/api/v1` |
| `API_TIMEOUT` | Default HTTP request timeout (ms) | `30000` |
| `API_KEY` | Header API key placeholder | `your_api_key_here` |
| `BEARER_TOKEN` | Bearer auth token placeholder | `your_bearer_token_here` |
| `DB_HOST` | SQL database hostname | `localhost` |
| `DB_PORT` | SQL database port | `5432` |
| `DB_NAME` | SQL database name | `freshlife_qa` |
| `DB_USER` | SQL database user | `qa_user` |
| `DB_PASSWORD` | SQL database password | `qa_password_placeholder` |
| `MONGODB_URI` | MongoDB Atlas connection URI | `mongodb+srv://...` |
| `MONGODB_DATABASE` | MongoDB database name | `freshlife_db` |
| `MONGODB_COLLECTION` | Target MongoDB collection | `users` |

> [!CAUTION]
> Never commit `.env` or hardcoded credentials to Git. `.env` is listed in `.gitignore`.

---

## Test Execution

Execute tests using Pytest markers registered in `pytest.ini`:

- **Run all tests**:
  ```bash
  pytest
  ```

- **Run UI tests only**:
  ```bash
  pytest -m ui
  ```

- **Run API tests only**:
  ```bash
  pytest -m api
  ```

- **Run Database tests only**:
  ```bash
  pytest -m db
  ```

- **Run Smoke test suite**:
  ```bash
  pytest -m smoke
  ```

- **Run Regression test suite**:
  ```bash
  pytest -m regression
  ```

- **Run a specific test file**:
  ```bash
  pytest ui_tests/test_home_ui.py
  ```

- **Run in headed browser mode (Playwright)**:
  ```bash
  pytest -m ui --headed
  ```

- **Run tests in parallel (pytest-xdist)**:
  ```bash
  pytest -n auto
  ```

- **Run tests and collect Allure results**:
  ```bash
  pytest --alluredir=reports/allure-results
  ```

---

## Allure Reports

To generate and view Allure test reports locally:

1. **Run tests with Allure output**:
   ```bash
   pytest --alluredir=reports/allure-results
   ```

2. **Generate and open the Allure HTML report**:
   ```bash
   allure serve reports/allure-results
   ```

3. **Generate static HTML report**:
   ```bash
   allure generate reports/allure-results -o reports/allure-report --clean
   ```

---

## CI/CD Pipeline

The framework includes a GitHub Actions pipeline (`.github/workflows/test_runner.yml`) that automatically:
- Triggers on `push` and `pull_request` to `main` or `develop`, as well as on a daily cron schedule.
- Sets up Python 3.11 and installs requirements.
- Installs Playwright headless Chromium dependencies.
- Injects configuration from GitHub Repository Secrets.
- Executes smoke and regression tests.
- Uploads Allure results as workflow build artifacts.

---

## Database Validation Strategy

```
+-------------------+      HTTP/Browser      +-----------------------+
|  Playwright / API | ---------------------> | Application Under Test|
+-------------------+                        +-----------------------+
          |                                              |
          | Assert State                                 | Persist State
          v                                              v
+-------------------+                        +-----------------------+
|  Pytest Database  | <--------------------- |  SQL / MongoDB Atlas  |
|  Validation Layer |       Fetch Data       +-----------------------+
+-------------------+
```

1. **Action Execution**: Playwright performs a UI workflow (e.g. user signup) or API client submits a payload.
2. **Backend Mutation**: The application under test processes the request and writes state changes to PostgreSQL and MongoDB Atlas.
3. **Database Validation**: Pytest executes SQL queries via `SQLClient` and MongoDB document searches via `MongoDBClient`.
4. **Assertion**: Results from the backend database are asserted against expected state to ensure data integrity.

---

## Test Data Strategy

- **Static Data**: Stored as structured JSON files inside `test_data/` (e.g. `sample_data.json`).
- **Data-Driven Tests**: Loaded directly into `@pytest.mark.parametrize` decorators to run identical test logic against multiple datasets.
- **Dynamic Secrets & Configs**: Injected at runtime via `.env` file or environment variables parsed by `config/settings.py`.

---

## Coding Standards

- **PEP 8**: Strict adherence to standard Python code formatting.
- **Type Hints**: All functions, methods, and class attributes must include explicit Python type hints.
- **Locators**: Prefer role-based, text-based, or `data-testid` selectors over fragile XPath expressions.
- **Test Isolation**: Every test must be independent, self-contained, and clean up its state where applicable.

---

## Contribution & Maintenance

1. Create a feature branch (`git checkout -b feature/new-test-suite`).
2. Ensure all tests pass locally (`pytest`).
3. Maintain code clean-up and formatting standards.
4. Submit a Pull Request targeting `main`.
