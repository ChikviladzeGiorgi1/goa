def generate_big_sentence(name, surname, age):
 
    sentence = "Hello, my name is {} {} and I am {} years old.".format(name, surname, age)
    return sentence


name = input("Please enter your first name: ")
surname = input("Please enter your last name: ")
age = input("Please enter your age: ")


result = generate_big_sentence(name, surname, age)

print(result)

def my_split(main_string, string_to_split):

    result = main_string.split(string_to_split)

    print(result)


main_string = input("Please enter the main string: ")
string_to_split = input("Please enter the string to split by: ")


my_split(main_string, string_to_split)