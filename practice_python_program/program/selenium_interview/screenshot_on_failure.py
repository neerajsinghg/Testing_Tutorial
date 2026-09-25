"""
Interview Question: How do you capture a screenshot automatically when a Pytest test fails?

Senior Interview Explanation:
"I use the Pytest `pytest_runtest_makereport` hook to detect test failures.
When the call phase fails, I retrieve the WebDriver fixture from `item.funcargs` and save a screenshot
named after the test. In a CI pipeline, I publish the screenshot as a build artifact and integrate it with Allure/HTML reports."
"""

import pytest
from pathlib import Path
from selenium import webdriver

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            screenshot_dir = Path("screenshots")
            screenshot_dir.mkdir(exist_ok=True)

            file_name = f"{item.name}.png"
            screenshot_path = screenshot_dir / file_name

            driver.save_screenshot(str(screenshot_path))
            print(f"\n[Pytest Hook] Screenshot saved: {screenshot_path}")

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_login_demo(driver):
    driver.get("https://example.com")
    assert "Invalid Expected Title" in driver.title
