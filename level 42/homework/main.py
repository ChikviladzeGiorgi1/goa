  # 1)

# key - dictionary-ს გასაღები(ობიექტის დამახასიათებელი თვისება)
# value - key-ის მნიშვნელობა(რაც ინახება კონკრეტულ key-ში)

# 2,3,4) 

user = {
    "username": "John",
    "email": "example@gmail.com",
    "password": "12345",
    "phone": "555-555-555",
    "age": 20
}

print(user.keys())
print(user.values())
print(user.items())

print("-------------------------")

# 5)

for i in user.items():
    print(i[0])

# 6)

if "username" in user:
    print(True)
else:
    print(False)

print("-------------------------")

# 7)

if "email" in user:
    print(user.get("email"))

# 8)

user["passcode"] = "1234"

print(user)

# 9)

user.pop("phone")
print(user)

# 10)

user1 = {
    "username": "Bob",
    "country": "Georgia"
}

user.update(user1)

print(user)

# 11)

print(len(user))

# 12)

my_dict = {
    "name": "John",
    "age": 25,
    "height": 175,
    "isProgramer": True
}

sum = 0

for i in my_dict.values():
    if type(i) == int:
        sum += i

print(sum)

# 13)

user.clear()

print(user)
 

 #14) 
my_dict = {
    "name": "Nika",
    "unsername": "chikviladze",
    "age": 25,
    "height": 178,
    "isProgramer": True,
    "phone": 555 666 777,
    "location": "Tbilisi",
    "gender" : "boy",


}
 
 
     


