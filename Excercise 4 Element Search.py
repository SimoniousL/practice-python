def SearchNumber(list, wanted_number):
    for i in list:
        if i == wanted_number:
            print(f'{wanted_number} is inside the list.')

def BinarySearchNumber(list, wanted_number):
    sort(list)
    

list_a = [1, 2, 3, 4, 5]

SearchNumber(list_a, 6)