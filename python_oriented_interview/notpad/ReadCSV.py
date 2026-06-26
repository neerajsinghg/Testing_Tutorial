import os
import csv

# We use relative path to Book1csv.csv or current directory csv file
possible_paths = [
    r"F:\Testing_Tutorial\python_oriented_interview\notpad\book1csv.csv",
    r"F:\Testing_Tutorial\practice_java_program\notpad\Book1csv.csv",
    r"book1csv.csv",
    r"../notpad/book1csv.csv"
]

file_path = None
for path in possible_paths:
    if os.path.exists(path):
        file_path = path
        break

if file_path is None:
    # Default to current directory name
    file_path = "book1csv.csv"

try:
    with open(file_path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            print(",".join(row))
except FileNotFoundError as e:
    print(f"File not found: {file_path}")
except Exception as e:
    print(e)
