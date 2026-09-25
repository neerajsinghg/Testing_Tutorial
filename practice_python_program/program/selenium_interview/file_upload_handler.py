"""
Interview Question: How do you upload a file using Selenium Python?

Interview Explanation:
"If the HTML contains a standard `<input type='file'>`, I locate the input element and send the absolute file path directly using `element.send_keys(file_path)`.
I do not click the upload element directly because that triggers the native OS file-picker dialog, which Selenium cannot control."
"""

from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By

def upload_file_demo(file_path_str: str = "sample.pdf"):
    driver = webdriver.Chrome()
    try:
        driver.get("https://example.com")
        file_path = Path(file_path_str).resolve()

        # Code pattern:
        # file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
        # file_input.send_keys(str(file_path))

        print(f"[File Upload Concept] Uploaded file directly via send_keys('{file_path.name}') on input[type=file]")
    finally:
        driver.quit()

if __name__ == "__main__":
    upload_file_demo()
