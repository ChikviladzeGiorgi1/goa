#2) თქვენი სიტყვებით ახსენით რა არის ციკლი და იტერაცია
# ციკლი (loop) პროგრამირების კონცეფციაა, რომელიც უზრუნველყოფს გარკვეული კოდის გამეორებას რამდენჯერმე, სანამ არ შესრულდება კონკრეტული პირობა.
# იტერაცია (iteration) ნიშნავს ერთ ციკლში შემავალი თითოეული ნაბიჯის შესრულებას.
# 4) შექმენით დიაპაზონი 20-დან 50-მდე და შეინახეთ ცვლადში
range_20_to_50 = range(20,51)
print(list(range_20_to_50))

range_100_to_150 = range(100, 151)
print(list(range_100_to_150))

even_nums=range(20,51, 2)
print(list(even_nums))

odd_nums=range(11,32, 2)
print(list(odd_nums))

for i in range(10):
    print("giorgi chikviladze")
    
for i in range(10,31):
    print(i / 2)

for i in range(40, 61):
    print(i**3)

for _ in range(5):
    num=int(input("enter your"))
    print(num)   

name=input("enter your name: ")
for i in name:
    print(i)

num1=int(input("enter your num1: "))
num2=int(input("enter your num2: "))
num3=int(input("enter your num3: "))
for i in range(num1,num2,num3):
    print(i**2)
    
sum=0
for i in range(5,16):
    sum+=i
print(sum)
