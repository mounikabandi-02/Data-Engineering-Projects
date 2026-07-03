import csv

total_salary = 0
employee_count = 0

with open("employees.csv", "r") as file:
    reader = csv.DictReader(file)

    print("Employee Records")
    print("----------------")

    for row in reader:
        print(f"{row['Name']} - {row['Department']} - ${row['Salary']}")
        total_salary += int(row["Salary"])
        employee_count += 1

average_salary = total_salary / employee_count

print("\nTotal Employees:", employee_count)
print("Average Salary:", average_salary)
