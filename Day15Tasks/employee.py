class Employee:

    def __init__(self):
        self.employees = {}

    def add_employee(self):
        try:
            emp_id = input("Enter ID: ")
            name = input("Enter name: ")
            salary = int(input("Enter salary: "))

            self.employees[emp_id] = {
                "name": name,
                "salary": salary
            }

            print("Added successfully")

        except ValueError:
            print("Invalid salary entry")

    def display_emp(self):
        for emp_id, details in self.employees.items():
            print("ID:", emp_id)
            print("Name:", details["name"])
            print("Salary:", details["salary"])
            print()

    def save_to_file(self):
        try:
            with open("employees.txt", "w") as file:
                for emp_id, details in self.employees.items():
                    file.write(
                        f"{emp_id}, {details['name']}, {details['salary']}\n"
                    )

            print("Data saved successfully.")

        except Exception as e:
            print("File error:", e)


emp = Employee()

for i in range(3):
    emp.add_employee()

print("\nEmployee Details:")
emp.display_emp()

emp.save_to_file()