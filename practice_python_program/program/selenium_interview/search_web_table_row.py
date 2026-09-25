"""
Interview Question: How do you find a specific row in a dynamic web table and click an action button inside that row?

Interview Explanation:
"I iterate over table rows `rows = driver.find_elements(By.XPATH, '//table//tbody/tr')`.
For each row, I extract the target column cell text. Once matched, I use relative XPath `.//button[contains(text(), 'Edit')]`
(noting the leading dot `.` which scopes search inside the current row element) to click the action button."

Important XPath Concept:
`".//button"` searches inside the current row element, whereas `"//button"` searches the entire page DOM.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By

def find_row_and_click_action(target_name: str = "Neeraj"):
    driver = webdriver.Chrome()
    try:
        driver.get("https://example.com")
        rows = driver.find_elements(By.XPATH, "//table//tbody/tr")

        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            if len(cells) > 1 and cells[1].text.strip() == target_name:
                print(f"Found row for '{target_name}': {row.text}")
                edit_button = row.find_element(By.XPATH, ".//button[contains(text(),'Edit')]")
                edit_button.click()
                break
    finally:
        driver.quit()

if __name__ == "__main__":
    print("[Web Table] Demonstrating relative XPath .// row element search.")
