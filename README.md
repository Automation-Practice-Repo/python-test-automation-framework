# Python Test Automation Framework

Enterprise-grade Python test automation framework with Playwright (UI), Selenium (UI), REST API testing, PostgreSQL & MongoDB Atlas validation, Allure reporting, and GitHub Actions CI/CD.

## Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?style=flat&logo=pytest&logoColor=white)
![Playwright](https://img.shields.io/badge/Playwright-45BA4C?style=flat&logo=playwright&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=flat&logo=selenium&logoColor=white)
![REST API](https://img.shields.io/badge/REST%20API-6DB33F?style=flat&logo=api&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=flat&logo=postgresql&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-2088FF?style=flat&logo=github-actions&logoColor=white)
![Allure](https://img.shields.io/badge/Allure-FF6C37?style=flat&logo=allure&logoColor=white)

## Features

- **Multi-Tool Support**: Playwright, Selenium WebDriver, Python Requests
- **Page Object Model**: Reusable page components with encapsulation
- **Pytest Fixtures**: Session, module, function, and class-scoped fixtures
- **Data-Driven Testing**: JSON, YAML, CSV test data support
- **API Testing**: RESTful API validation with comprehensive assertions
- **Database Validation**: PostgreSQL and MongoDB Atlas connectivity
- **Parallel Execution**: Pytest-xdist for distributed test execution
- **Allure Reporting**: Rich interactive test reports
- **CI/CD Integration**: GitHub Actions and Jenkins pipelines

## Project Structure

```
python-test-automation-framework/
├── config/
│   ├── config.yaml              # Application configuration
│   ├── environments/            # Environment-specific settings
│   └── test_data/               # Test data files
├── src/
│   ├── pages/                   # Page Object Model classes
│   │   ├── base_page.py        # Base page with common methods
│   │   └── components/         # Reusable UI components
│   ├── api/                     # API testing modules
│   │   ├── clients/            # API client implementations
│   │   └── assertions/         # Custom API assertions
│   ├── db/                      # Database utilities
│   │   ├── postgres_client.py  # PostgreSQL operations
│   │   └── mongo_client.py     # MongoDB operations
│   ├── core/                    # Framework core
│   │   ├── driver_manager.py   # WebDriver management
│   │   ├── fixtures.py         # Pytest fixtures
│   │   └── reporting.py        # Reporting utilities
│   └── utils/                  # Helper utilities
├── tests/
│   ├── ui/                     # UI test suites
│   ├── api/                    # API test suites
│   ├── integration/            # Integration test suites
│   └── db/                     # Database test suites
├── reports/                     # Test reports and logs
├── requirements.txt
├── pyproject.toml
├── pytest.ini
└── README.md
```

## Installation

```bash
# Clone the repository
git clone https://github.com/Automation-Practice-Repo/python-test-automation-framework.git
cd python-test-automation-framework

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install Playwright browsers (if using UI automation)
playwright install chromium
```

## Configuration

Edit `config/config.yaml`:

```yaml
environment: staging
base_url: "https://your-app-url.com"
api_base_url: "https://api.your-app-url.com"

database:
  postgres:
    host: "localhost"
    port: 5432
    database: "test_db"
    user: "test_user"
    password: "test_pass"
  mongodb:
    connection_string: "mongodb://localhost:27017"
    database: "test_db"

reporting:
  allure_results: "reports/allure-results"
  html_report: "reports/html"

execution:
  parallel_workers: 4
  screenshot_on_failure: true
  video_on_failure: true
```

## Running Tests

```bash
# Run all tests
pytest

# Run with specific markers
pytest -m ui
pytest -m api
pytest -m integration

# Run with Allure reporting
pytest --alluredir=reports/allure-results
allure serve reports/allure-results

# Run in parallel
pytest -n auto

# Run specific test file
pytest tests/ui/test_login.py -v

# Run with tags
pytest -k "smoke" -v
```

## Test Data

Test data is managed in `config/test_data/`:

```json
{
  "users": {
    "admin": {
      "username": "admin@test.com",
      "password": "Test@123",
      "role": "admin"
    },
    "standard": {
      "username": "user@test.com",
      "password": "Test@123",
      "role": "user"
    }
  }
}
```

## Page Object Example

```python
from src.pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "loginBtn")
    ERROR_MESSAGE = (By.CLASS_NAME, "error-message")

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, username, password):
        self.enter_text(self.USERNAME_INPUT, username)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)
```

## API Testing Example

```python
import pytest
import requests
from src.api.clients.api_client import APIClient

class TestAuthAPI:
    @pytest.fixture
    def api_client(self):
        return APIClient(base_url="https://api.example.com")

    def test_login_success(self, api_client):
        response = api_client.post("/auth/login", {
            "username": "test@example.com",
            "password": "Test@123"
        })
        assert response.status_code == 200
        assert "token" in response.json()
```

## CI/CD Integration

### GitHub Actions

The framework includes `.github/workflows/ci.yml` for:
- Linting with ruff
- Type checking with mypy
- Running tests
- Generating Allure reports
- Uploading test artifacts

## Contributing

1. Fork the repository
2. Create a feature branch
3. Write tests for new functionality
4. Ensure all tests pass
5. Submit a pull request

## License

MIT License - See LICENSE file for details

---

**Author:** Hareesh Chowdary  
**Email:** haree.06a@gmail.com  
**GitHub:** [automation-harish](https://github.com/Automation-Practice-Repo)
