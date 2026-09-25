"""
Interview Question: How do you handle single and nested iframes in Selenium?

Interview Explanation:
"Selenium can interact with elements inside an iframe only after switching the driver's context to that iframe using `driver.switch_to.frame()`.
For nested frames, I switch frame by frame (`frame('iframe1')` then `frame('iframe2')`).
To return one level back, I use `parent_frame()`. To return to the main document, I use `default_content()`."
"""

from selenium import webdriver
from selenium.webdriver.common.by import By

def demonstrate_iframe_handling():
    driver = webdriver.Chrome()
    try:
        driver.get("https://httpbin.org")

        # Code pattern for single iframe:
        # iframe = driver.find_element(By.ID, "payment-frame")
        # driver.switch_to.frame(iframe)
        # driver.find_element(By.ID, "card-number").send_keys("4111111111111111")
        # driver.switch_to.default_content()

        # Code pattern for nested iframe:
        # driver.switch_to.frame("iframe1")
        # driver.switch_to.frame("iframe2")
        # driver.find_element(By.ID, "username").send_keys("Neeraj")
        # driver.switch_to.default_content()

        print("[IFrame Concept] Switched to iframe, performed actions, returned to default_content().")
    finally:
        driver.quit()

if __name__ == "__main__":
    demonstrate_iframe_handling()
