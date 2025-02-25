def multiply(a, b):
  return a * b

def even_or_odd(number):
    if number %2 == 0:
        return "Even"
    else: return "Odd"

def number_to_string(num):
    return str(num)

def solution(string):
    return string[::-1]


def make_negative( number ):
    result = 0
    if number > 0:
      result = number - number *2
    else:
        return number
    return result



def opposite(number):
    return -number


def bool_to_word(boolean):
    if boolean == True:
        return "Yes"
    elif boolean == False:
        return "No"
    
def positive_sum (arr):
    result = 0

    for i in arr:
        if i > 0:
            result += i
    return result
        
def repeat_str(repeat, string):
    return repeat * string

def remove_char(s):
    return s [1:-1]        
     

def square_sum(numbers):
    result = 0
    for i in numbers:
        result += i **2
    return result     