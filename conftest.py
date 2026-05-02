import os
import pytest
from selenium import webdriver
from dotenv import load_dotenv
from selenium.webdriver.chrome.options import Options

from screenshot_utility import take_screenshot

load_dotenv()
@pytest.fixture()
def driver():
    opts = Options()
    # Required for CI
    opts.add_argument("--headless=new")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")

    # Good for stable automation
    opts.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile_password_manager_enabled": False,
        "profile.password_manager_leak_detection": False
    })

    driver = webdriver.Chrome(options=opts)
    yield driver
    driver.quit()
    driver = webdriver.Chrome(options=opts)
    driver.maximize_window()

    yield driver
    driver.quit()

@pytest.fixture()
def get_baseurl():
    url = os.getenv("BASE_URL")
    if not url:
        raise ValueError("BASE_URL is not set in .env file")
    return url

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    # Take screenshot only if test FAILED during test execution
    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver")

        if driver:
            take_screenshot(driver, f"FAILED_{item.name}")


@pytest.fixture()
def get_credentials():
    return {
             "username" : os.getenv("SAUCE_USERNAME"),
             "password" : os.getenv("SAUCE_PASSWORD")
    }