"""
Factory Design Pattern for Browser Driver Instantiation
Senior SDET Context: Decouples driver creation logic from test execution code, supporting Chrome, Firefox, Edge, and Headless modes.
"""

from typing import Protocol

class BrowserDriver(Protocol):
    def launch(self) -> str: ...
    def close(self) -> None: ...

class ChromeDriver:
    def launch(self) -> str:
        return "Chrome Driver Started"
    def close(self) -> None:
        print("Chrome Driver Closed")

class FirefoxDriver:
    def launch(self) -> str:
        return "Firefox Driver Started"
    def close(self) -> None:
        print("Firefox Driver Closed")

class EdgeDriver:
    def launch(self) -> str:
        return "Edge Driver Started"
    def close(self) -> None:
        print("Edge Driver Closed")

class DriverFactory:
    @staticmethod
    def get_driver(browser_type: str) -> BrowserDriver:
        drivers = {
            "chrome": ChromeDriver,
            "firefox": FirefoxDriver,
            "edge": EdgeDriver,
        }
        driver_cls = drivers.get(browser_type.lower())
        if not driver_cls:
            raise ValueError(f"Unsupported browser type: {browser_type}")
        return driver_cls()

if __name__ == "__main__":
    for browser in ["chrome", "firefox", "edge"]:
        driver = DriverFactory.get_driver(browser)
        print(f"[{browser.upper()}] ->", driver.launch())
        driver.close()
