"""
Interview Question: How do you implement reusable explicit waits in Selenium Python?

Interview Explanation:
"I create a reusable `WaitHelper` wrapper class around `WebDriverWait` and `expected_conditions`.
Explicit waits synchronize execution with the actual browser state, avoiding brittle `time.sleep()` calls.
Key conditions include `visibility_of_element_located`, `element_to_be_clickable`, and `presence_of_element_located`."
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class WaitHelper:
    def __init__(self, driver, timeout: int = 20):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def wait_for_visible(self, locator: tuple[str, str]):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_clickable(self, locator: tuple[str, str]):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def wait_for_presence(self, locator: tuple[str, str]):
        return self.wait.until(EC.presence_of_element_located(locator))

if __name__ == "__main__":
    from selenium import webdriver
    driver = webdriver.Chrome()
    try:
        driver.get("https://example.com")
        wait = WaitHelper(driver, timeout=10)
        heading = wait.wait_for_visible((By.TAG_NAME, "h1"))
        print("Located heading text:", heading.text)
    finally:
        driver.quit()
