# 1)

names = ["Nika", "Dato", "Luka", "Vano", "Soso", "Rati"]

for i in range(len(names)): # 0, 1, 2, 3, 4, 5
    if i % 2 == 0:
        print(names[i])

# 2)

numbers = [10, 20, 30, 40, 50]

numbers[3] = 100

print(numbers)

# 3)

numbers = [10, 20, 30, 40, 50]

num1 = int(input("Please enter the first number: "))
num2 = int(input("Please enter the second number: "))

if num1 > num2:
    print(numbers[num2: num1 + 1])
elif num2 > num1:
    print(numbers[num1: num2 + 1])
else:
    print([])