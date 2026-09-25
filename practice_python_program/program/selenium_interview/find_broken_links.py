"""
Interview Question: How do you find broken links on a web page using Selenium and Python?

Interview Explanation:
"I first collect all anchor elements using `find_elements(By.TAG_NAME, 'a')`.
I extract the `href` attribute and then use the Requests library to send an HTTP request.
If the response status code is 400 or above, I consider the link broken. I also handle invalid URLs and request exceptions."

Important Note: Don't use Selenium itself to validate HTTP status codes. Selenium verifies browser behavior;
`requests` is more appropriate for HTTP-level validation.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

def check_broken_links(url: str = "https://httpbin.org"):
    driver = webdriver.Chrome()
    try:
        driver.get(url)
        links = driver.find_elements(By.TAG_NAME, "a")
        print(f"Total links found: {len(links)}")

        for link in links:
            href = link.get_attribute("href")
            if not href or not href.startswith("http"):
                continue

            try:
                response = requests.get(href, timeout=5, allow_redirects=True)
                if response.status_code >= 400:
                    print(f"Broken Link: {href} | Status: {response.status_code}")
                else:
                    print(f"Valid Link: {href} | Status: {response.status_code}")
            except requests.RequestException as error:
                print(f"Unable to access {href}: {error}")
    finally:
        driver.quit()

if __name__ == "__main__":
    check_broken_links()
