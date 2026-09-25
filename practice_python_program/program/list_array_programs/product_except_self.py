"""
Interview Question:
Given an array `nums`, return an array `output` such that `output[i]` is equal to the product of all elements of `nums` except `nums[i]`, without using division and in O(n) time.

Interview Explanation:
Division is disallowed to prevent divide-by-zero errors when array contains 0s and to test prefix/suffix array products algorithm design.

Key Concepts:
1. Prefix product array: stores cumulative product of elements to the left of `i`.
2. Suffix product variable: multiplies cumulative product of elements to the right of `i`.
3. Time Complexity: O(n), Space Complexity: O(1) auxiliary space (excluding output array).
"""


def product_except_self(nums: list) -> list:
    """
    Computes product of array except self in O(n) time without division.
    """
    n = len(nums)
    output = [1] * n

    # Step 1: Calculate left prefix products
    prefix = 1
    for i in range(n):
        output[i] = prefix
        prefix *= nums[i]

    # Step 2: Multiply right suffix products on the fly
    suffix = 1
    for i in range(n - 1, -1, -1):
        output[i] *= suffix
        suffix *= nums[i]

    return output


if __name__ == "__main__":
    sample_nums = [1, 2, 3, 4]

    result = product_except_self(sample_nums)
    print(f"Input Array:  {sample_nums}")
    print(f"Product Except Self: {result}")
