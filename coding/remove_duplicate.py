from collections import Counter


def remove_duplicate(ar):
    """
    remove duplicate from an array
    INPUT - [2, 3, 1, 5, 6, 4, 4, 2]
    OUTPUT - [1, 3, 5, 6]
    """
    my_non_duplicate_arr = []
    dict_number_count = Counter(ar)
    print("dictionary: " + str(dict_number_count))
    # keys are in alphabetical order
    print("after remove one element of duplicate number and sort: " + str(dict_number_count.keys()))

    index = 0
    # Finding no. of occurrence of a number and get the index of it.
    for number_frequency in dict_number_count.values():
        # all the indexes from the keys which have value greater than 1.
        if number_frequency == 1:
            # keys are in alphabetical order
            my_non_duplicate_arr.append(dict_number_count.keys()[index])
        index = index + 1

    print my_non_duplicate_arr


remove_duplicate([2, 3, 1, 5, 6, 4, 4, 2])
