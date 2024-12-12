num1 = int(input("enter your num: "))
num2 = int(input("enter your num: "))
print(max(num1 , num2))

number = int(input("enter your num: "))
if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")

    num1 = float(input("Enter number: "))
if num1 > 0:
    print(num1, "is positive")
else:
    print(num1, "is negative")

num = float(input("Enter number: "))
if num % 5 == 0:
    print(num, "is divisible by five")
else:
    print(num, "is not divisible by five")

num = int(input("Enter number: "))

if num % 2 == 0:
    print(num, "is even")
else:
    print(num, "is odd")

correct_pas = "Goa best"
count = 0
user_password = input("Enter password: ")

while user_password != correct_pas:
    count += 1
    user_password = input("Enter password: ")
print("Correct password!")
print("You needed", count, "tries")

num1 = float(input("Enter the first number: "))
operator = input("Enter the operator (+, -, *, /): ")
num2 = float(input("Enter the second number: "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."
else:
    result = "Invalid operator!"

print("Result:", result)