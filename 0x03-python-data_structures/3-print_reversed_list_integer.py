def print_reversed_list_integer(my_list=[]):
    if my_list:
        my_list.reverse()
        for el in my_list:
            print('{:d}'.format(el))
