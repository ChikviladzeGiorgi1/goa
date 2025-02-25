def greet():
    return("hello world!")

def count_sheeps(sheep):
    sum = 0
    for i in sheep:
        if i == True:
            sum += 1
    return sum           

def no_space(x):
    result = x.replace(" ","")
    return result

def double_integer(i):
    return i * 2

def greet(name):
    return "Hello,"+ " " + name + " how are you doing today"