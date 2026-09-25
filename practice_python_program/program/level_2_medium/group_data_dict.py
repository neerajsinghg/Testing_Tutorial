"""
27. Group Data Using Dictionary
Interview Note: Uses setdefault() to group items under shared department/category keys.
Time Complexity: O(n)
Space Complexity: O(n)
"""

def group_by_department(employees: list[dict]) -> dict[str, list[str]]:
    result = {}
    for employee in employees:
        dept = employee["dept"]
        result.setdefault(dept, []).append(employee["name"])
    return result

if __name__ == "__main__":
    employees = [
        {"name": "Amit", "dept": "QA"},
        {"name": "Neeraj", "dept": "QA"},
        {"name": "Rahul", "dept": "Dev"}
    ]
    print("Grouped Data:", group_by_department(employees))
