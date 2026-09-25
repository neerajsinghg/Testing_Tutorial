"""
Mutable Default Argument Pitfall
Interview Question: Why does passing a default mutable object (like value=[]) retain state across calls?
Explanation: Default argument values are evaluated ONCE when the function definition is executed, not at each call.
To fix: Use `value=None` and initialize `if value is None: value = []`.
"""

def test_buggy(value=[]):
    value.append(1)
    return value

def test_fixed(value=None):
    if value is None:
        value = []
    value.append(1)
    return value

if __name__ == "__main__":
    print("Buggy default calls:")
    print("Call 1:", test_buggy())
    print("Call 2:", test_buggy())

    print("\nFixed default calls:")
    print("Call 1:", test_fixed())
    print("Call 2:", test_fixed())
