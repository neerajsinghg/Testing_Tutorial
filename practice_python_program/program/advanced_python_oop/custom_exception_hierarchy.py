"""
Framework Custom Exception Hierarchy
Senior SDET Context: Defines specialized, structured exceptions (`FrameworkError`, `ElementNotFoundException`, `APIResponseMismatchError`) with contextual metadata.
"""

class FrameworkError(Exception):
    """Base exception for automation framework errors."""
    def __init__(self, message: str, step_name: str = ""):
        super().__init__(message)
        self.message = message
        self.step_name = step_name

    def __str__(self):
        prefix = f"[{self.step_name}] " if self.step_name else ""
        return f"{prefix}{self.message}"

class ElementNotFoundException(FrameworkError):
    def __init__(self, locator: tuple[str, str], timeout: int = 10):
        loc_type, loc_val = locator
        msg = f"Element located by ({loc_type}='{loc_val}') not visible after {timeout}s timeout."
        super().__init__(msg, step_name="UI Exception")

class APIResponseMismatchError(FrameworkError):
    def __init__(self, field: str, expected: str, actual: str):
        msg = f"API Field '{field}' mismatch | Expected: '{expected}', Actual: '{actual}'"
        super().__init__(msg, step_name="API Assertion")

if __name__ == "__main__":
    try:
        raise ElementNotFoundException(("id", "submit_button"), timeout=15)
    except ElementNotFoundException as e:
        print("Caught UI Exception:", e)

    try:
        raise APIResponseMismatchError("status", "200", "500")
    except APIResponseMismatchError as e:
        print("Caught API Exception:", e)
