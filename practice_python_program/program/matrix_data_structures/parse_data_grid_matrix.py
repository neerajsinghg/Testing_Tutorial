"""
Matrix Transposition & Data Grid Manipulation
Senior SDET Context: Transposes web table rows into columns (or vice versa) to validate UI grid alignment and report formatting.
"""

def transpose_matrix(matrix: list[list]) -> list[list]:
    if not matrix:
        return []
    rows = len(matrix)
    cols = len(matrix[0])
    return [[matrix[r][c] for r in range(rows)] for c in range(cols)]

if __name__ == "__main__":
    data_grid = [
        ["Header1", "Header2", "Header3"],
        ["Val1",    "Val2",    "Val3"],
        ["Val4",    "Val5",    "Val6"]
    ]
    print("Original Data Grid:")
    for row in data_grid:
        print(row)

    print("\nTransposed Data Grid:")
    for row in transpose_matrix(data_grid):
        print(row)
