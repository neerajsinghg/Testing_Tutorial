"""
Interview Question: How do you scroll to an element and highlight it using JavaScript in Selenium?

Interview Explanation:
"I use JavaScript execution via `driver.execute_script()`.
- Scroll element into view: `driver.execute_script('arguments[0].scrollIntoView({block: \"center\"});', element)`
- Highlight element: `driver.execute_script('arguments[0].style.border=\"3px solid red\";', element)`
- Scroll to bottom: `driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')`"
"""

from selenium import webdriver
from selenium.webdriver.common.by import By

def demonstrate_scroll_and_highlight():
    driver = webdriver.Chrome()
    try:
        driver.get("https://www.wikipedia.org")
        element = driver.find_element(By.ID, "js-link-box-en")

        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        print("Scrolled element into view.")

        driver.execute_script("arguments[0].style.border='3px solid red';", element)
        print("Highlighted element with red border.")
    finally:
        driver.quit()

if __name__ == "__main__":
    demonstrate_scroll_and_highlight()
