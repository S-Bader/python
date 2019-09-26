from datetime import date


class Employee:
    def __init__(self, name, age, salary, employment_date):
        self.name = name
        self.age = age
        self.salary = salary
        self.employment_date = employment_date

    def get_working_years(self):
        return date.today() - self.employment_date


class Manager(Employee):
    def __init__(self, name, age, salary, employment_date, bonus_percentage):
        self.name = name
        self.age = age
        self.salary = salary
        self.employment_date = employment_date
        self.bonus_percentage = bonus_percentage

    def get_working_years(self):
        return date.today() - self.employment_date

    def get_bonus(self):
        return self.bonus_percentage * self.salary


normal_employees = []

managers = []


options = ["Show Employees", "Show Managers", "Add an Employee", "Add a Manager", "Exit"]

print("Option:")


for option in options:
    index = options.index(option) +1
    print(index ,"- " + option)

user_option = int(input("What would you like to do? "))

while user_option != 5:
    if user_option == 1:
        print(normal_employees)
    elif user_option == 2:
        print(managers)
    elif user_option == 3:
        

     





















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