employees = []

for i in range(3):
    print(f"\nEmployee {i + 1}")
    emp_name = input("Enter name: ")
    emp_age = int(input("Enter age: "))
    emp_salary = float(input("Enter salary: "))
    employees.append((emp_name, emp_age, emp_salary))

print("\nEmployees list:", employees)
