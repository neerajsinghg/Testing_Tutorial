"""
Dynamic Base Page Object Pattern Component
Senior SDET Context: Provides reusable base page abstraction with dynamic locator resolution, waiting mechanisms, and element interactions.
"""

from typing import Any

class BasePage:
    def __init__(self, driver: Any):
        self.driver = driver

    def find_element(self, locator_type: str, locator_value: str) -> str:
        # Mock element finding logic
        return f"Element<{locator_type}={locator_value}>"

    def click(self, locator: tuple[str, str]) -> None:
        loc_type, loc_val = locator
        element = self.find_element(loc_type, loc_val)
        print(f"Clicked on {element}")

    def type_text(self, locator: tuple[str, str], text: str) -> None:
        loc_type, loc_val = locator
        element = self.find_element(loc_type, loc_val)
        print(f"Typed '{text}' into {element}")

class LoginPage(BasePage):
    USERNAME_INPUT = ("id", "username")
    PASSWORD_INPUT = ("id", "password")
    LOGIN_BUTTON = ("xpath", "//button[@type='submit']")

    def login(self, username: str, password: str) -> None:
        self.type_text(self.USERNAME_INPUT, username)
        self.type_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

if __name__ == "__main__":
    login_page = LoginPage(driver=None)
    login_page.login("admin@example.com", "SecretPass123!")
