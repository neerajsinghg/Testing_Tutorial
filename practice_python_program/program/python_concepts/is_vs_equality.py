"""
Difference Between `is` and `==`
Interview Question: What is the difference between `==` and `is` in Python?
Explanation:
- `==` checks Value Equality (do objects hold the same content?).
- `is` checks Identity Equality (do variables point to the exact same memory address?).
"""

def demonstrate_is_vs_equals():
    a = [1, 2, 3]
    b = [1, 2, 3]

    print("a == b (Value check):", a == b)
    print("a is b (Identity check):", a is b)
    print("id(a) == id(b):", id(a) == id(b))

if __name__ == "__main__":
    demonstrate_is_vs_equals()
