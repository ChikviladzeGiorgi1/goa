for i in range(20):
    print("giorgi chikviladze")
    # საკლასო დავალება:

#3მომხმარებელს შემოატანინეთ რიცხვი და შეინახეთ მთელი რიცხვის სახით. იგივე გაიმეორეთ მემეორე ცვლადზე.

#for ციკლით იტერაცია მოახდინეთ დიაპაზონზე, რომლის საწყისი რიცხვია პირველი ცვლადი და საბოლოო რიცხვია მეორე ცვლადი.

#ციკლის ყოველ იტერაციაზე დაბეჭდეთ საიტერაციო ცვლადის კვადრატი
num1 = int(input("enter your num: "))
num2 = int(input("enter your num2: "))

for i in range(num1, num2 + 1):
    print(f"{i} kvadrati aris: {i**2}")

n = int(input("enter your number: "))

for i in range(1, n + 1):
    print(f"the square of {i} is: {i**2}")
