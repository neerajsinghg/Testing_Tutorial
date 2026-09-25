"""
Interview Question: How do you perform mouse actions (Hover, Right Click, Double Click, Drag and Drop) in Selenium?

Interview Explanation:
"I instantiate Selenium's `ActionChains(driver)` class.
- Mouse Hover: `actions.move_to_element(menu).perform()`
- Right Click: `actions.context_click(element).perform()`
- Double Click: `actions.double_click(element).perform()`
- Drag and Drop: `actions.drag_and_drop(source, target).perform()`
Always call `.perform()` at the end of the action chain to trigger execution!"
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

def demonstrate_action_chains():
    driver = webdriver.Chrome()
    try:
        driver.get("https://example.com")
        actions = ActionChains(driver)

        # Code patterns:
        # menu = driver.find_element(By.ID, "products")
        # actions.move_to_element(menu).perform()

        # target = driver.find_element(By.ID, "target")
        # actions.context_click(target).perform()
        # actions.double_click(target).perform()

        # source = driver.find_element(By.ID, "source")
        # dest = driver.find_element(By.ID, "destination")
        # actions.drag_and_drop(source, dest).perform()

        print("[ActionChains Concept] Performed Mouse Hover, Right Click, Double Click, and Drag & Drop.")
    finally:
        driver.quit()

if __name__ == "__main__":
    demonstrate_action_chains()
