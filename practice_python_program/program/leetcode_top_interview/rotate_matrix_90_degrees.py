"""
Interview Question: How do you rotate an N x N 2D matrix 90 degrees clockwise in-place in Python?

Interview Explanation:
"I achieve in-place 90-degree clockwise rotation in two steps:
1. Transpose the matrix: Swap `matrix[r][c]` with `matrix[c][r]` for `r < c`.
2. Reverse each row: `matrix[r].reverse()`.
This operates in O(N^2) time and O(1) auxiliary space."
"""

def rotate_matrix_90_degrees(matrix: list[list[int]]) -> None:
    n = len(matrix)
    for r in range(n):
        for c in range(r + 1, n):
            matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

    for r in range(n):
        matrix[r].reverse()

if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print("Original Matrix:")
    for row in matrix:
        print(row)

    rotate_matrix_90_degrees(matrix)
    print("\nRotated 90 Degrees Clockwise:")
    for row in matrix:
        print(row)
