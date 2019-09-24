skills = ["Juggling", "Sword Fighting","Knitting", "Acting", "Managing Money", "Loving" ]

cv = {}

print("Welcome to the special recruitment program, please answer the following questions: ")
print()
cv["name"] = input("what is your name?  ")
cv["age"] = int(input("what is your age?  "))
cv["experience"] = int(input("how many years of experience do you have?  "))

cv["skills"] = []



print()

print("Skills:")
print()
for skill in skills:
	index = skills.index(skill) +1
	print(index ,"- " + skill)

print()

index_one = int(input("Choose a skill from above by entering its number: ")) -1

cv["skills"].append(skills[index_one]) 

index_two = int(input("Choose another skill from above by entering its number: ")) -1

cv["skills"].append(skills[index_two]) 

print() 


criteria_1 = cv["age"] > 21 and cv["age"] < 65
criteria_2 = cv["experience"] >= 2

if criteria_1 and criteria_2 and ("Loving" in cv['skills'] or "Managing Money" in cv["skills"]) == True:

	print("You have been accepted, %s." % cv["name"])
else:
	print("Apologies %s, but we cannot accept you at this time... too bad, soo sad. :(" % cv["name"])









# Create a list called skills and fill it with any skills of your choice. These are the skills that the user will choose from.
# Create an empty dictionary called cv. This dictionary will then hold all of the applicant's information.
# Ask the user for their name. Save the name in the dictionary with key name.
# Ask the user for their age. Save the age in the dictionary with key age.
# Ask the user for their years of experience. Save the years of experience in the dictionary with key experience.
# Add a key skills to the cv dictionary and give it an empty list as a value.
# Print the skills from the skills list and number them from 1. where 1 will have the first skill in the list (which has index 0).
# Ask the user to choose a skill from the list. Then get the skill from the skills list and add it to the skills list in the cv dictionary.
# Ask the user for another skill and append it to the skills list in the cv dictionary.
# This next part will completely depend on you. This is where you set the criteria for acceptance. For example, you can set that the applicant has to be older than 25, has at least 2 years experience, and has a specific skill. Check for the applicant credentials and notify them of the result.
# Note: In the the example code above, the acceptance criteria was:

# Age more than 25 and less than 40.
# Experience years has to be more than 3.
# Python has to be one of the skills


# Welcome to the special recruitment program, please answer the following questions:
# What's your name? Kale Salad
# How old are you? 30
# How many years of experience do you have? 6

# Skills:
# 1- Python
# 2- C++
# 3- Javascript
# 4- Juggling
# 5- Running
# 6- Eating

# Choose a skill from above by entering its number: 1
# Choose another skill from above by entering its number: 6
# You have been accepted, Kale Salad.