# import os

# base_dir = os.path.dirname(__file__)  # folder of the script
# file_path = os.path.join(base_dir, "..", "files", "reading_file_example.txt")
# print(base_dir)
# with open(file_path, "a") as f:
#     f.write("\nThis is third line of the text")
# with open(file_path, "r") as r:
#     print(r.read())





















import os

base_dir = os.path.dirname(__file__)
file_path = os.path.join(base_dir, "..", "data", "countries_data.json")
abs_path = os.path.abspath(file_path)
print(base_dir)
print(abs_path)

with open(abs_path, "r", encoding="utf-8") as f:
    print(f.read())