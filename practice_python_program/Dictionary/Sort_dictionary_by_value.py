salary = {
    "Amit": 50000,
    "Neeraj": 90000,
    "Rahul": 70000,
    "Vikas": 60000
}

sorted_salary = dict(sorted(salary.items(), key=lambda item: item[1]))
print("Sorted salary by value:", sorted_salary)

def sort_dict_by_value(d):
    return dict(sorted(d.items(), key=lambda item: item[1]))

sorted_salary = sort_dict_by_value(salary)  
print("Sorted salary by value (function):", sorted_salary)

def sort_dict_by_value1(d):
    return dict(sorted(d.items(), key=lambda item: item[1], reverse=True))

sorted_salary_desc = sort_dict_by_value1(salary)
print("Sorted salary by value (descending):", sorted_salary_desc)

