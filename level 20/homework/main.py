# 1)

# elif - (სხვა შემთხვევაში თუ) მისი მეშვეობით შეგვიძლია შევქმნათ პირობა(if-ის მსგავსად), რომლის მიხედვითაც სასურველი კოდი გაეშვება ან არა.

# 2)

num1 = int(input("Please enter the fist number: "))
num2 = int(input("Please enter the second number: "))
num3 = int(input("Please enter the third number: "))

if num1 > num2 and num1 > num3:
    print(num1)
elif num2 > num1 and num2 > num3:
    print(num2)
elif num3 > num1 and num3 > num2:
    print(num3)


# 3)

score = int(input("Please enter your score: "))

if score >= 90 and score <= 100:
    print("A")
elif score >= 80 and score < 90:
    print("B")
elif score >= 70 and score < 80:
    print("C")
elif score >= 60 and score < 70:
    print("D")
else:
    print("F")


# 4)

num = int(input("Please enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# 5)

num1 = int(input("Please enter the fist number: "))
num2 = int(input("Please enter the second number: "))

sum = 0
for i in range(num1 + 1, num2):
    sum += i

print(sum)

# 6,7

numbers = [10, 20, 30, 40, 50]
print(numbers[0])
print(numbers[1])
print(numbers[-1])

print(numbers)