#1 Homework
num = input("Enter a number")

if num.isdigit():
    print(f"You entered : {num}")
else:
    print("Error: That's Not Even a Number.")
   # 2 Homework
my_list = [10, 20, 30]
Index = 10

if Index < len(my_list):
    print(my_list[Index])
else:
    print("Error: That index is not in the list.")
#3 Homework
a = "Hello"
b = 5

if isinstance(a, str) and isinstance(b, str):
    result = a + b
    print(result)
else:
    print("Error: You can only add two strings together.")
