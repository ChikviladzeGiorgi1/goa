# While (ციკლი) ციკლი იწყება, როცა პროგრამა ამოწმებს მოცემულ პირობას. ეს არის ლოგიკური გამოთვლა (True/False), რომელიც შეიძლება იყოს ნებისმიერი არგუმენტი.
# 3) თქვენი სიტყვებით ახსენით განსხვავება while და for ციკლებს შორის
# for ციკლში პირდაპირ გვაქვს მოცემული განსაზღვრული რიცხვი თუ რამდენჯერ უნდა დავპრინტოთ, ხოლო while-ში გამოთვლებია საჭირო
for i in range(50):
    print("GOA BEST ! ! !")

i = 0
while i < 50:
    print("GOA BEST ! ! !")
    i += 1

i = 1
while i < 10 + 1:
    print(i)
    i += 1

i = 1
while i < 20 + 1:
    print(i)
    i += 2

i = 10
while i > 0:
    print(i)
    i -= 1
print("blast off !")

correct_password = "paroli"
counter = 0
password_correct = False
while not password_correct:
    user_password = input("enter your password: ")
    counter += 1
    if user_password == correct_password:
        correct_password = True
        print("accses grainted")
        print(f"the password has been enterd {counter}")
    else:
        print("password is incorrect")
        
correct_username = "user 123"
correct_password = "gio123"

username = input("enter your username: ")
password = input("enter your password: ")

while username != correct_username or password != correct_password:
    print("incorrect username or password. try again")
    username = input("enter your username: ")
    password = input("enter your password: ")

print("Login completed")




