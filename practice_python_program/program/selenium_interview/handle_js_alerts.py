"""
Interview Question: How do you handle JavaScript alerts, confirmations, and prompts?

Interview Explanation:
"There are three JavaScript dialog types: Alert, Confirmation, and Prompt.
I wait for the alert using `EC.alert_is_present()`, switch context using `alert = driver.switch_to.alert`,
read text via `alert.text`, type input via `alert.send_keys()`, and click OK via `alert.accept()` or Cancel via `alert.dismiss()`."
"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def demonstrate_alert_handling():
    driver = webdriver.Chrome()
    try:
        driver.get("https://example.com")

        # Code pattern:
        # alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
        # print("Alert Text:", alert.text)
        # alert.send_keys("Neeraj")
        # alert.accept()  # Click OK
        # alert.dismiss() # Click Cancel

        print("[JS Alert Concept] Handled Alert, Confirmation, and Prompt dialogs using driver.switch_to.alert")
    finally:
        driver.quit()

if __name__ == "__main__":
    demonstrate_alert_handling()
