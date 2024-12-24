 # 1)

numbers = [1,2,3,4,5,6,7,8,9,10]

num = int(input("Please enter a number: "))

if num >= 0 and num < len(numbers):
    print(numbers[num])
elif num >= len(numbers) * -1 and num <= -1:
    print(numbers[num])

# 2)

list1 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
for x in list1:
    print(x*2)
    print(x/2)

    
