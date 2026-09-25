"""
36. Find Maximum Salary by Department
Interview Note: Tracks employee dictionary with highest salary per department in a single pass.
Time Complexity: O(n)
Space Complexity: O(d) where d is number of unique departments.
"""

def find_max_salary_by_dept(employees: list[dict]) -> dict:
    highest = {}
    for employee in employees:
        dept = employee["dept"]
        if dept not in highest or employee["salary"] > highest[dept]["salary"]:
            highest[dept] = employee
    return highest

if __name__ == "__main__":
    employees = [
        {"name": "Amit", "dept": "QA", "salary": 60000},
        {"name": "Neeraj", "dept": "QA", "salary": 90000},
        {"name": "Rahul", "dept": "Dev", "salary": 80000},
        {"name": "Vikas", "dept": "Dev", "salary": 100000}
    ]
    print("Highest Salary per Dept:", find_max_salary_by_dept(employees))
