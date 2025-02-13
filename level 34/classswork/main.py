def list (main_list,indexes_list):
    new_list = []
    for i in range(len(main_list)):
        if i not  in indexes_list:
            new_list.append(main_list[i])
    return new_list

def remove_one_element(list,index):
 del list[index]
 return list