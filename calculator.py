first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

operation = input("Choose the operation (+, -, /, *): ")

if operation == "+":
	print("the answer is ", first_number + second_number)

elif operation == "-":
	print("the answer is ", first_number - second_number)

elif operation == "/":
	print("the answer is ", first_number / second_number)

elif operation == "*":
	print("the answer is ", first_number * second_number)

else:
	print("Invalid operation.")
