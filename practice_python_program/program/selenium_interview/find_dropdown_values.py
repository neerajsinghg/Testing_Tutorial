"""
Interview Question: How do you retrieve all values from a standard HTML dropdown?

Interview Explanation:
"For standard HTML `<select>` dropdowns, I wrap the WebElement in Selenium's `Select` class.
I iterate over `dropdown.options` to print or extract all option text strings.
Options can also be selected using `select_by_visible_text()`, `select_by_value()`, or `select_by_index()`."

Interview Point:
`Select` works with standard `<select>` tags. It does NOT directly work with custom dropdowns built using `div`, `li`, etc.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def print_dropdown_options(url: str = "https://www.wikipedia.org"):
    driver = webdriver.Chrome()
    try:
        driver.get(url)
        dropdown_element = driver.find_element(By.ID, "searchLanguage")
        dropdown = Select(dropdown_element)

        print("Total languages in dropdown:", len(dropdown.options))
        for option in dropdown.options[:5]:  # Print first 5
            print(f"Option Text: '{option.text}' | Value: '{option.get_attribute('value')}'")

        dropdown.select_by_value("en")
        print("Selected language: English")
    finally:
        driver.quit()

if __name__ == "__main__":
    print_dropdown_options()
