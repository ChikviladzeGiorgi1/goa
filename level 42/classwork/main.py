# initializing the dictionary
my_dict = {
    'name': 'გიორგი',
    'surname': 'მარიამიძე',
    'academy': 'თბილისის სახელმწიფო უნივერსიტეტი',
    'fav-color': 'ლურჯი',
    'city': 'თბილისი',
    'goa-student': True,
    'age': 22,
    'fav-programming-lang': 'Python'
}
print("Name:", my_dict['name'])
print("Surname:", my_dict['surname'])
print("Academy:", my_dict['academy'])
print("Favorite Color:", my_dict['fav-color'])
print("City:", my_dict['city'])
print("GOA Student:", my_dict['goa-student'])
print("Age:", my_dict['age'])
print("Favorite Programming Language:", my_dict['fav-programming-lang'])



# Initializing a dictionary with at least five key-value pairs
my_dict = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York',
    'job': 'Engineer',
    'hobby': 'Photography'
}
print("Keys in the dictionary:", my_dict.keys())
print("Values in the dictionary:", my_dict.values())
print("Key-Value pairs in the dictionary:", my_dict.items())
print("\nIterating over the dictionary:")
for key, value in my_dict.items():
    print(f"The key '{key}' has the value '{value}'")


