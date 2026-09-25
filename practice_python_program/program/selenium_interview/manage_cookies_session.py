"""
Interview Question: How do you add, read, and delete cookies in Selenium, and how do you bypass login UI using cookies?

Interview Explanation:
"To manage cookies:
- Add cookie: `driver.add_cookie({'name': 'session_id', 'value': 'ABC123'})`
- Get all cookies: `driver.get_cookies()`
- Delete cookie: `driver.delete_cookie('session_id')` or `driver.delete_all_cookies()`
To bypass UI login: I navigate to the domain (`driver.get('https://example.com')`), inject a valid session cookie via `add_cookie()`, and refresh the page (`driver.refresh()`)."
"""

from selenium import webdriver

def demonstrate_cookie_management():
    driver = webdriver.Chrome()
    try:
        driver.get("https://example.com")

        driver.add_cookie({"name": "session_id", "value": "ABC123_EXAMPLE_TOKEN"})
        print("Added authentication cookie.")

        cookie = driver.get_cookie("session_id")
        print("Retrieved cookie:", cookie)

        driver.refresh()
        print("Refreshed page with injected cookie session.")

        driver.delete_cookie("session_id")
        print("Deleted session cookie.")
    finally:
        driver.quit()

if __name__ == "__main__":
    demonstrate_cookie_management()
