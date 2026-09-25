"""
Custom Context Manager for Automation Resources
Senior SDET Context: Uses `__enter__` and `__exit__` or `@contextmanager` to safely initialize and teardown browser sessions, DB connections, or temporary test artifacts.
"""

class BrowserSession:
    def __init__(self, browser_name: str = "chrome"):
        self.browser_name = browser_name
        self.driver = None

    def __enter__(self):
        print(f"[Context Manager] Starting {self.browser_name} browser session...")
        self.driver = f"WebDriver<{self.browser_name}>"
        return self.driver

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"[Context Manager] Teardown: Closing {self.browser_name} browser session...")
        if exc_type:
            print(f"[Context Manager] Exception caught during session: {exc_val}")
        self.driver = None
        return False

if __name__ == "__main__":
    with BrowserSession("chrome") as driver:
        print(f"Inside test block using {driver}")
