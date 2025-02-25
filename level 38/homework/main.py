my_tuple = (1,2,3,4,5)
second_last = my_tuple[-2]
middle = my_tuple[1:4]
print(second_last)
print(middle)

tuple123 = (10,15,20,25,30)
# იქნება ერორი 

tuple321 = (1,2,3,4,5)
a,b,c,d,e = tuple321
print(a)
print(b)
print(c)
print(d)
print(e)

tuple999 = (10,10,10,20,30,40,50,60,70)
count = tuple999.count(10)
print(count)
index = tuple999.index(10)
print(index)

set123 = {1,2,3,4,5}
set123.add(6)
set123.remove(1)
present = 4 in set123
print(set123)
print(present)


set1 = {1,2,3,4,5,}
set2 = {1,2,6,7,8,9,10}
union = set1 | set2
intesection = set1 & set2
deference = set1 - set2
print(union)
print(intesection)
print(deference)

list1 = [1,2,3,4,5,5,5,2,1,]
set10 = set(list1)
unique = list(set10)
print(unique)
