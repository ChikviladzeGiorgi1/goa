for i in range(0, 20 + 1, 2):
    print(i)
for i in range(1, 20 + 1, 2):
    print(i)
 
num1 = int(input("enter your num: "))
num2 = int(input("enter your num2"))
if num1 > num2:
    range1 = range(num2, num1 + 1)
    sum1 = 0

    for i in range1:
        if i % 2 == 0:
            print(i)
            sum1 += i
            
    print("Sum of all even numbers are:", str(sum1))
else:
    range2 = range(num1, num2 + 1)
    sum2 = 0

    for i in range2:
        if i % 2 != 0:
            print(i)
            sum2 += 1    
    print("Sum of all even numbers are:", str(sum2))




