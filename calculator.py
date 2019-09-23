first_number = input("Enter the first number: ")
second_number = input("Enter the second number: ")
operation = input("Choose the operation (+, -, /, *): ")

if first_number.isdigit() and second_number.isdigit():
	first_number = int(first_number)
	second_number = int(second_number)

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
