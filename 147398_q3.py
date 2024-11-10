#Employee and Department Management System
class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_details(self):
            """Display details of employee"""
            print(f"Name: {self.name}, Employee ID: {self.employee_id}, Salary: {self.salary}")

    def update_salary(self, new_salary):
            """Update salary of employee"""
            self.salary = new_salary
            print(f"Salary updated to {self.salary}")


class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.employees = []

    def add_employee(self, employee):
        """Add an employee to department"""
        self.employees.append(employee)
        print(f"Employee {employee.name} added to {self.department_name} department")

    def total_salary_expenditure(self):
        """Calculate and display the total salary expenditure for the department"""
        total_salary = sum(emp.salary for emp in self.employees)
        print(f"Total salary expenditure for {self.department_name} is: {total_salary}")

    def display_all_employees(self):
        """Display all employees in the department"""
        if not self.employees:
            print(f"No employees in the {self.department_name} department")
        else:
            print(f"Employees in {self.department_name} department:")
            for emp in self.employees:
                emp.display_details()


#Interactive input for adding employees to a department and displaying total expenditure
def main():
    department_name = input("Enter department name: ")
    department = Department(department_name)

    while True:
        add_employee = input("Do you want to add an employee to department? (y/n): ").lower()
        if add_employee == 'y':
            name = input("Enter employee name: ")
            employee_id = input("Enter employee ID: ")
            salary = float(input("Enter employee salary: "))

            employee = Employee(name, employee_id, salary)
            department.add_employee(employee)
        else:
            break

    department.display_all_employees()
    department.total_salary_expenditure()

if __name__ == "__main__":
    main()





