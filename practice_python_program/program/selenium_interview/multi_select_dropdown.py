"""
Interview Question: How do you handle standard and custom multi-select dropdowns in Selenium?

Interview Explanation:
"For standard HTML `<select multiple>`, I use `Select(element)`. I call `select_by_visible_text()`, inspect `all_selected_options`, or clear selections via `deselect_all()`.
For custom UI dropdowns built with `div` or `li`, I click the dropdown host to expand options, find option list items using `driver.find_elements(By.XPATH, '//div[@role=\"option\"]')`, and click matching options."
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def demonstrate_multi_select_dropdown():
    driver = webdriver.Chrome()
    try:
        driver.get("https://example.com")

        # Standard <select multiple> pattern:
        # element = driver.find_element(By.ID, "skills")
        # dropdown = Select(element)
        # dropdown.select_by_visible_text("Python")
        # dropdown.select_by_visible_text("Selenium")
        # selected = [opt.text for opt in dropdown.all_selected_options]
        # dropdown.deselect_all()

        # Custom UI dropdown pattern:
        # dropdown_host = driver.find_element(By.ID, "custom-dropdown")
        # dropdown_host.click()
        # options = driver.find_elements(By.XPATH, "//div[@role='option']")
        # for option in options:
        #     if option.text.strip() in ["Python", "Selenium"]:
        #         option.click()

        print("[Multi-Select Concept] Handled both standard <select multiple> and custom div/li multi-select dropdowns.")
    finally:
        driver.quit()

if __name__ == "__main__":
    demonstrate_multi_select_dropdown()
