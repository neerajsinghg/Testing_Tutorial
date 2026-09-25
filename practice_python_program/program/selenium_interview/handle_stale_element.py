"""
Interview Question: How do you handle `StaleElementReferenceException` in Selenium Python?

Interview Explanation:
"A stale element means the previously located WebElement is no longer attached to the current DOM (common after AJAX updates or DOM re-rendering).
I avoid storing long-lived WebElement references and store tuple locators instead (`(By.ID, 'submit')`).
For transient cases, I implement a retry function using a `try-except StaleElementReferenceException` loop."
"""

from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By

def click_with_retry(driver, locator: tuple[str, str], attempts: int = 3) -> bool:
    for attempt in range(attempts):
        try:
            element = WebDriverWait(driver, 10).until(
                lambda d: d.find_element(*locator)
            )
            element.click()
            return True
        except StaleElementReferenceException:
            if attempt == attempts - 1:
                raise
    return False

if __name__ == "__main__":
    print("[Stale Element] Demonstrating locator-based retry wrapper pattern.")
