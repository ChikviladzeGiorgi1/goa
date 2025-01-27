name = input("enter name")
name2 = input("არჩევანი(u ან l): ")
if name2 == "u":
    print(name.upper())  #
elif name2 == "l":
    print(name.lower())
else:
    print("wrong information")

    if index == -1:
        print(-1)
    else:
        print(index)

main_string = input("შეიყვანე მთავარი სთრინგი: ")
str_to_find = input("შეიყვანე საძიებელი სთრინგი: ")

manual_find(main_string, str_to_find)
