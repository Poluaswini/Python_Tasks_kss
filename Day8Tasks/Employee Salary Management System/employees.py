'''A company stores employee data in a file employees.txt in the format:
EmployeeName Salary
Example:
Ramesh 25000
Sita 30000
Arun 28000
Write a Python program that:
● Reads employee data from the file
● Displays all employee details
● Finds the employee with the highest salary
● Appends a new employee record to the file'''

file=open("employees.txt", "w")
file.write("aswi 25000\n")
file.write("Sathu 30000\n")
file.write("Aswitha 28000\n")
file.close()

file=open("employees.txt", "r")
highest_salary=0
highest_employee=""
print("Employee Details:")
for line in file:
    print(line.strip())
    data=line.split()
    name=data[0]
    salary=int(data[1])

    if salary>highest_salary:
        highest_salary=salary
        highest_employee=name

file.close()

print("\nEmployee with Highest Salary:")
print(highest_employee, highest_salary)

file=open("employees.txt", "a")
name=input("\nEnter employee name: ")
salary=input("Enter salary: ")
file.write(name + " " + salary + "\n")
file.close()

file=open("employees.txt", "r")
print("\nUpdated Employee Records:")
print(file.read())
file.close()