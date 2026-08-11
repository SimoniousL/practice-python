def CreateNewList(input_list):
    new_list = []
    new_list.append(input_list[0])
    new_list.append(input_list[-1])
    return new_list

print(CreateNewList(['5', '10', '15', '20', '25']))
