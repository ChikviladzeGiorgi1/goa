def hello ():
    print("hello")

def sum (num1,num2):
    result = num1+num2
    return result

def info1 (input):
    result = input * 10
    return result

def greeting (name):
    result = "hello" + name
    if not name:
        return"hello guests"
    else: return result 

def function1 ():
    print ("hello gio")
    def function2 ():
        print("goodbye gio")
    function2()
function1()         

def evenodd(list):
    for i in list:
        if i % 2 == 0:
            print("even")
        else: print("odd")

def maximum (list):
    return max(list)

def positive (list):
    sum = []
    for i in list:
        if i > 0:
            sum.append(i)
    return sum

def sum ():
    return sum(num for num in range(1,101)if num % 3 == 0)
    
            
