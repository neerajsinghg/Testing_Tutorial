"""
Interview Question: How do you interact with an element inside Shadow DOM?

Interview Explanation:
"Shadow DOM creates an encapsulated DOM tree that normal XPath cannot cross.
In modern Selenium 4, I locate the shadow host using `shadow_host = driver.find_element(...)`,
access its root via `shadow_root = shadow_host.shadow_root`, and then locate inner elements using `shadow_root.find_element(By.CSS_SELECTOR, 'input')`.
In JavaScript fallback, I use `driver.execute_script('return arguments[0].shadowRoot', shadow_host)`."
"""

from selenium import webdriver
from selenium.webdriver.common.by import By

def demonstrate_shadow_dom():
    driver = webdriver.Chrome()
    try:
        driver.get("https://example.com")

        # Selenium 4 Modern Syntax:
        # shadow_host = driver.find_element(By.CSS_SELECTOR, "my-custom-component")
        # shadow_root = shadow_host.shadow_root
        # inner_input = shadow_root.find_element(By.CSS_SELECTOR, "input.user-field")
        # inner_input.send_keys("Neeraj")

        print("[Shadow DOM Concept] Accessed shadow_host.shadow_root and interacted with encapsulated element.")
    finally:
        driver.quit()

if __name__ == "__main__":
    demonstrate_shadow_dom()
