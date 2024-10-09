# Creating a Simple Calculato
# Step one - creating a menu with arithmetic operation
print ("Welcome to Simple Calculator")
print ("choose an operation")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
# Asking the user to choose an operation

choice = input("Enter your choice (1-4)")
# Get two number from the user
num1 = float(input ("Enter the first number:"))
num2 = float(input ("Enter the second number:"))

#Perform the chosen operation
if choice == '1':
    result = num1 + num2
    print(f"Result: {num1} + {num2} = {result}")
elif choice == '2':
    result = num1 - num2
    print(f"Result: {num1} - {num2} = {result}")
elif choice == '3':
    result = num1 * num2
    print(f"Result: {num1} * {num2} = {result}")
elif choice == '4':
    if num2 == 0:
        print("Error: Division by zero is not allowed")
    else: result = num1 / num2
    print(f"Result: {num1} / {num2} = {result}")
else: 
    print("Invalid choice. Please select a valid operation")




        


