"""
Interview Question: How do you switch between multiple browser windows/tabs in Selenium?

Interview Explanation:
"`driver.current_window_handle` returns the handle of the current window.
`driver.window_handles` returns a list of all open window handles.
I iterate over `window_handles`, switch to the child window using `driver.switch_to.window(handle)`,
perform operations, close the child window, and return context to `parent_window`."
"""

from selenium import webdriver
from selenium.webdriver.common.by import By

def demonstrate_window_switch():
    driver = webdriver.Chrome()
    try:
        driver.get("https://example.com")
        parent_window = driver.current_window_handle
        print("Parent Window Handle:", parent_window)

        driver.execute_script("window.open('https://www.wikipedia.org', '_blank');")

        all_windows = driver.window_handles

        for window in all_windows:
            if window != parent_window:
                driver.switch_to.window(window)
                print("New Tab Title:", driver.title)
                driver.close()
                break

        driver.switch_to.window(parent_window)
        print("Back to Parent Window Title:", driver.title)
    finally:
        driver.quit()

if __name__ == "__main__":
    demonstrate_window_switch()
