"""
Shallow Copy Behavior
Interview Question: Why does mutating nested elements in a shallow copy affect the original list?
Explanation: `list.copy()` creates a new outer list container, but nested mutable elements (lists/dicts) share object references.
To fix: Use `copy.deepcopy()`.
"""

import copy

def demonstrate_shallow_copy():
    a = [[1, 2], [3, 4]]
    b = a.copy()
    b[0].append(100)
    print("Shallow Copy Output - Original 'a':", a)
    print("Shallow Copy Output - Copy 'b':", b)

def demonstrate_deep_copy():
    a = [[1, 2], [3, 4]]
    c = copy.deepcopy(a)
    c[0].append(100)
    print("Deep Copy Output - Original 'a':", a)
    print("Deep Copy Output - Deep Copy 'c':", c)

if __name__ == "__main__":
    demonstrate_shallow_copy()
    print("-" * 30)
    demonstrate_deep_copy()
