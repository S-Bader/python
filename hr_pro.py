from datetime import date


class Employee:
    def __init__(self, name, age, salary, employment_date):
        self.name = name
        self.age = age
        self.salary = salary
        self.employment_date = employment_date

    def get_working_years(self):
        return date.today().year - int(self.employment_date)

    def __str__(self):
        return "Name: %s, Age: %s, Salary: %s, Working Years: %s" % (self.name, self.age, self.salary, self.get_working_years())


class Manager(Employee):
    def __init__(self, name, age, salary, employment_date, bonus_percentage):
        super().__init__(name, age, salary, employment_date)
        self.bonus_percentage = bonus_percentage

    def get_bonus(self):
        return float(self.bonus_percentage) * float(self.salary)

    def __str__(self):
        return "Name: %s, Age: %s, Salary: %s, Working Years: %s, Bonus: %.3f" % (self.name, self.age, self.salary, self.get_working_years(), self.get_bonus())


normal_employees = []

managers = []

print("Welcome to HR Pro")
print()
print("""
Options:
    1. Show Employees
    2. Show Managers
    3. Add An Employee
    4. Add A Manager
    5. Exit
""")

choice = int(input("What would you like to do? "))

while choice != 5:
    if choice == 1:
        for employee in normal_employees:
            print(employee)
    elif choice == 2:
        for manager in managers:
            print(manager)
    elif choice == 3:
        name = input("Employee Name: ")
        age = input("Age: ")
        salary =  input("Salary: ")
        employment_date = input("Date of Employment: ")
        employee = Employee(name, age, salary, employment_date)
        normal_employees.append(employee)
    elif choice == 4:
        name = input("Manager Name: ")
        age = input("Age: ")
        salary =  input("Salary: ")
        employment_date = input("Date of Employment: ")
        bonus_percentage = input("Bonus: ")
        manager = Manager(name, age, salary, employment_date, bonus_percentage)
        managers.append(manager)

    print("""
    Options:
        1. Show Employees
        2. Show Managers
        3. Add An Employee
        4. Add A Manager
        5. Exit
    """)

    choice = int(input("What would you like to do? "))


     





















# In this task you'll be creating the HR system for a company. This company has two types of employees: normal employees and managers.

# The following example assume the current year is 2019.

# For this task you need to create two classes:

# Employee:

# name
# age
# salary
# employment_date
# get_working_years()
# today - employement_date


 # Manager:

# name
# age
# salary
# employment_date
# bonus_percentage
# get_working_years()
# today - employement_date
# get_bonus()
# bonus_percentage * salary
# Define two empty lists: one for normal employees and one for managers.

# Print the options to the HR employee (the user).
# If 1 was chosen, print the employees information (the employees list).
# If 2 was chosen, print the managers information (the managers list).
# If 3 was chosen, allow the HR employee to add a normal employee to the system (the employees list).
# If 4 was chosen, allow the HR employee to add a manager to the system (the managers list).
# If 5 was chosen, stop the program.
# Push your code.