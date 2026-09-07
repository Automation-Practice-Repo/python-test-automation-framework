"""Pytest fixtures for test automation framework."""
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
import os
import yaml


def load_config():
    """Load configuration from config.yaml."""
    config_path = os.path.join(os.path.dirname(__file__), "../../config/config.yaml")
    with open(config_path, "r") as f:
        return yaml.safe_load(f)


@pytest.fixture(scope="session")
def config():
    """Load test configuration."""
    return load_config()


@pytest.fixture(scope="session")
def browser_config(config):
    """Browser configuration from config."""
    return config.get("browser", {})


@pytest.fixture(scope="function")
def chrome_driver(browser_config):
    """Chrome WebDriver fixture."""
    options = webdriver.ChromeOptions()
    if browser_config.get("headless", True):
        options.add_argument("--headless")
    if browser_config.get("disable_extensions", True):
        options.add_argument("--disable-extensions")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(browser_config.get("implicit_wait", 10))
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def firefox_driver(browser_config):
    """Firefox WebDriver fixture."""
    options = webdriver.FirefoxOptions()
    if browser_config.get("headless", True):
        options.add_argument("--headless")

    service = FirefoxService(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service, options=options)
    driver.implicitly_wait(browser_config.get("implicit_wait", 10))
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def edge_driver(browser_config):
    """Edge WebDriver fixture."""
    options = webdriver.EdgeOptions()
    if browser_config.get("headless", True):
        options.add_argument("--headless")

    service = EdgeService(EdgeChromiumDriverManager().install())
    driver = webdriver.Edge(service=service, options=options)
    driver.implicitly_wait(browser_config.get("implicit_wait", 10))
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def driver(request):
    """Dynamic driver fixture based on browser parameter."""
    browser = request.param if hasattr(request, "param") else "chrome"
    config = load_config()
    browser_cfg = config.get("browser", {})

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        if browser_cfg.get("headless", True):
            options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        if browser_cfg.get("headless", True):
            options.add_argument("--headless")
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=options)
    else:
        options = webdriver.EdgeOptions()
        if browser_cfg.get("headless", True):
            options.add_argument("--headless")
        service = EdgeService(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service, options=options)

    driver.implicitly_wait(browser_cfg.get("implicit_wait", 10))
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def api_base_url(config):
    """API base URL from config."""
    return config.get("api_base_url")


@pytest.fixture
def api_client(api_base_url):
    """API client fixture."""
    from src.api.clients.api_client import APIClient
    return APIClient(base_url=api_base_url)


@pytest.fixture(scope="session")
def db_config(config):
    """Database configuration."""
    return config.get("database", {})


@pytest.fixture
def postgres_client(db_config):
    """PostgreSQL client fixture."""
    from src.db.postgres_client import PostgresClient
    pg_config = db_config.get("postgres", {})
    client = PostgresClient(
        host=pg_config.get("host"),
        port=pg_config.get("port"),
        database=pg_config.get("database"),
        user=pg_config.get("user"),
        password=pg_config.get("password")
    )
    yield client
    client.close()


@pytest.fixture
def mongo_client(db_config):
    """MongoDB client fixture."""
    from src.db.mongo_client import MongoClient
    mongo_config = db_config.get("mongodb", {})
    client = MongoClient(connection_string=mongo_config.get("connection_string"))
    yield client
    client.close()
