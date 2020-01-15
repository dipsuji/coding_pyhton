def remove_duplicate_num(my_arr):
    """
    Remove duplicate number from an array
    INPUT - [2, 3, 4, 4, 5, 6, 2]
    OUTPUT - [2, 3, 4, 5, 6]
    """
    # making a empty array
    result_array = []
    # making a dictionary, key is number and value is occurrence of number
    num_dic = {}
    for num_element in my_arr:
        #  check number in num_dic
        if num_element in num_dic:
            # if num_element already in num_dic then increase counting but in intial there are no any element
            num_dic[num_element] += 1
        else:
            # if num_element not in num_dic then put its counting as 1
            num_dic[num_element] = 1
            # and that character append in array
            result_array.append(num_element)
    # print num_dic
    print result_array


remove_duplicate_num([2, 3, 4, 4, 5, 6, 1, 2])
