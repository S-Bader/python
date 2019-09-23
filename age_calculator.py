import datetime
current_date = datetime.date.today()

def check_birthdate(year, month, day):
	birthdate = datetime.date(year, month, day)
	if birthdate >= current_date:
		return False
	else:
		return True

def calculate_age(year, month, day):
	birthdate = datetime.date(year, month, day) 
	age = current_date - birthdate
	age_in_years = age.days // 365
	remaining_days = age.days % 365
	age_in_months = remaining_days // 30
	age_in_days = remaining_days % 30
	if age_in_years <= 0:
		print("Hey, No time travellers allowed!")
	else:
		print("You are %s years, %s months, %s days old." % (age_in_years,age_in_months ,age_in_days))

get_year = int(input("What year were you born? "))
get_month = int(input("What is your birth month? "))
get_day = int(input("what day were you born? "))


if check_birthdate == 0:
	print("Invalid birthdate.")
else:
	calculate_age(get_year,get_month,get_day)









'''Create a function and name it "check_birthdate":
Takes the year, month, and day as parameters.
Returns False if the given birthdate is in the future and True if it was in the past.
Create another function and name it "calculate_age":
Takes the year, month, and day as parameters.
Calculates the age of the user.
Prints a message to the user with their age in years.
This function does not return anything.
Ask the user for his birthdate (year, month, day)
Using the check_birthdate function:
If True was returned, call the calculate_age function.
If False was returned, print a message to the user that the birthdate is invalid.'''