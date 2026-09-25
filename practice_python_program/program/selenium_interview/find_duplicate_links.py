"""
Interview Question: How do you identify duplicate links on a webpage?

Interview Explanation:
"I collect all `a` elements and iterate over their `href` attributes.
Using a Python `set()` provides O(1) average lookup time. As I iterate, if a URL is already present
in the `seen` set, I add it to the `duplicates` set. This avoids O(n^2) list searches."

Why set()?
A set provides average O(1) membership checking instead of O(n) linear scan in lists.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By

def find_duplicate_links(url: str = "https://example.com"):
    driver = webdriver.Chrome()
    try:
        driver.get(url)
        links = driver.find_elements(By.TAG_NAME, "a")

        seen = set()
        duplicates = set()

        for link in links:
            href = link.get_attribute("href")
            if not href:
                continue

            if href in seen:
                duplicates.add(href)
            else:
                seen.add(href)

        print(f"Total unique URLs: {len(seen)}")
        print("Duplicate Links:")
        for dup in duplicates:
            print(" -", dup)
    finally:
        driver.quit()

if __name__ == "__main__":
    find_duplicate_links()
