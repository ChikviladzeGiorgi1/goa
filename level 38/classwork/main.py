my_tuple = (1,2,3,4,5,6,7,8,9,10)
for i in range(len(my_tuple)):
    print(my_tuple[i])


def no_duplicates(user_list):
    return list(set(user_list))   

numbers = [1,1,1,3,3,4,5,6,6,6,8,8,8,8,5,5,]
print(no_duplicates(numbers)) 