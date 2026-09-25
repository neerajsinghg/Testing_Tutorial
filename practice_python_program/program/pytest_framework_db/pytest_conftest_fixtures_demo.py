"""
Interview Question: How do you structure Pytest fixtures, conftest.py, and parametrized tests in automation frameworks?

Interview Explanation:
"I define shared fixtures in `conftest.py` with appropriate scope (`function`, `module`, `session`).
I use `yield` to separate setup code (before yield) and teardown code (after yield).
I use `@pytest.mark.parametrize` to run a test function against multiple input data sets."
"""

import pytest

@pytest.fixture(scope="session")
def api_auth_token():
    print("\n[Setup - Session Scope] Fetching global Auth Token...")
    token = "Bearer global_session_token_123"
    yield token
    print("\n[Teardown - Session Scope] Invalidating global Auth Token...")

@pytest.fixture(scope="function")
def database_connection():
    print("[Setup - Function Scope] Opening DB connection...")
    db = {"connected": True}
    yield db
    print("[Teardown - Function Scope] Closing DB connection...")

@pytest.mark.parametrize("user_id, expected_status", [
    (101, "active"),
    (102, "inactive"),
    (103, "active")
])
def test_user_status(user_id, expected_status, api_auth_token):
    assert api_auth_token.startswith("Bearer ")
    assert user_id > 100
    print(f"Validated user_id {user_id} with token successfully.")

if __name__ == "__main__":
    print("Pytest Conftest & Fixtures framework structure ready.")
