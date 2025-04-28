#Beginner Series #2 Clock
def past(h, m, s):
    sum_of_seconds = 0
    
    # hour -> second
    sum_of_seconds += h * 3600
    
    # minute -> second
    sum_of_seconds += m * 60
    
    # second
    sum_of_seconds += s
    
    # result
    result = sum_of_seconds * 1000
    
    return result 

#Abbreviate a Two Word Name
def abbrev_name(name):
    new_list = name.split(" ")
    return f"{new_list[0][0].upper()}.{new_list[1][0].upper()}"



#A Needle in the Haystack
def find_needle(haystack):
    result = haystack.index("needle")
    return f"found the needle at position {result}"


#Calculate average
def find_average(numbers):
    if not numbers: return 0
    return sum(numbers) / len(numbers)


#Invert values
def invert(lst):
    new_list=[]
    for i in lst:
        new_list.append(i * -1)
    return new_list

#Sentence Smash
def smash(words):
    return " ".join(words)


#Beginner - Reduce but Growdef grow(arr):
def grow(arr):
    product = 1

    for i in arr:
        product *= i

    return product



#Is he gonna survive?
def hero(bullets, dragons):
    if bullets >= dragons * 2: return True
    return False
def hero(bullets, dragons):
    return bullets >= dragons * 2


#How good are you really?
def better_than_average(class_points, your_points):
    other_avg = sum(class_points) / len(class_points)


def count_positives_sum_negatives(arr):
    if arr == []:
        return []

    counter = 0
    sum_negative = 0
    for i in arr:
        if i > 0:
            counter += 1 
        elif i < 0:
            sum_negative += i
    result = [counter,sum_negative]
    if result != [0,0]:
        return result
    return [0,0]

def dna_to_rna(dna):
    return dna.replace("T", "U")

def bmi(weight, height):
    bmi_value = weight / height ** 2

    if bmi_value <= 18.5: return "Underweight"
    elif bmi_value <= 25.0: return "Normal"
    elif bmi_value <= 30.0: return "Overweight"
    return "Obese"


#Beginner Series #2 Clock
def past(h, m, s):
    sum_of_seconds = 0
    
    # hour -> second
    sum_of_seconds += h * 3600
    
    # minute -> second
    sum_of_seconds += m * 60
    
    # second
    sum_of_seconds += s
    
    # result
    result = sum_of_seconds * 1000
    
    return result 

#Abbreviate a Two Word Name
def abbrev_name(name):
    new_list = name.split(" ")
    return f"{new_list[0][0].upper()}.{new_list[1][0].upper()}"



#A Needle in the Haystack
def find_needle(haystack):
    result = haystack.index("needle")
    return f"found the needle at position {result}"


#Calculate average
def find_average(numbers):
    if not numbers: return 0
    return sum(numbers) / len(numbers)


#Invert values
def invert(lst):
    new_list=[]
    for i in lst:
        new_list.append(i * -1)
    return new_list

#Sentence Smash
def smash(words):
    return " ".join(words)


#Beginner - Reduce but Growdef grow(arr):
def grow(arr):
    product = 1

    for i in arr:
        product *= i

    return product



#Is he gonna survive?
def hero(bullets, dragons):
    if bullets >= dragons * 2: return True
    return False
def hero(bullets, dragons):
    return bullets >= dragons * 2


#How good are you really?
def better_than_average(class_points, your_points):
    other_avg = sum(class_points) / len(class_points)


def count_positives_sum_negatives(arr):
    if arr == []:
        return []

    counter = 0
    sum_negative = 0
    for i in arr:
        if i > 0:
            counter += 1 
        elif i < 0:
            sum_negative += i
    result = [counter,sum_negative]
    if result != [0,0]:
        return result
    return [0,0]

def dna_to_rna(dna):
    return dna.replace("T", "U")

def bmi(weight, height):
    bmi_value = weight / height ** 2

    if bmi_value <= 18.5: return "Underweight"
    elif bmi_value <= 25.0: return "Normal"
    elif bmi_value <= 30.0: return "Overweight"
    return "Obese"


