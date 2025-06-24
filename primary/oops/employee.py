class Employee:
        def __init__(self, id, name, salary, dept):
            self.id = id
            self.name = name
            self.salary = salary
            self.dept = dept

        def calculate_emp_salary(self, hours_worked):
            overtime = hours_worked - 50
            overtime_amount = overtime * (self.salary / 50)
            self.salary += overtime_amount
            return self.salary

        def emp_assign_department(self, new_dept):
            self.dept = new_dept
            return self.dept

        def print_employee_details(self):
            return "{} with emp id: {} is in {} department, drawing {}"\
                .format(self.name, self.id, self.dept, self.salary)

employee1 = Employee(name="ADAMS", id="E7876", salary=50000, dept="ACCOUNTING")
employee2 = Employee(name="JONES", id="E7499", salary=45000, dept="RESEARCH")
employee3 = Employee(name="MARTIN", id="E7900", salary=50000, dept="SALES")
employee4 = Employee(name="SMITH", id="E7698", salary=55000, dept="OPERATIONS")


print("Original Employee Details: ")
print(employee1.print_employee_details())
print(employee2.print_employee_details())
print(employee3.print_employee_details())
print(employee4.print_employee_details())

print("Change Department of employee1 and employee4")
employee1.emp_assign_department("OPERATIONS")
employee4.emp_assign_department("SALES")

print("Calculate salary of employee2 and employee4 for overtime")
employee2.calculate_emp_salary(52)
employee4.calculate_emp_salary(60)

print("Modified Employee Details: ")
print(employee1.print_employee_details())
print(employee2.print_employee_details())
print(employee3.print_employee_details())
print(employee4.print_employee_details())
