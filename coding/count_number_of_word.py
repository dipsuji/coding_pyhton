def num_word(my_str):
    """
    count number of word in string sentence
    INPUT - This is testing program
    OUTPUT - 4
    """
    count = 0
    for i in range(len(my_str)):
        # search space at each position
        if my_str[i] == " ":
            count = count + 1
    return count + 1


print(num_word("This is testing program"))


def count_words(my_str):
    """
    count number of word in string sentence by using string spilt function.
    INPUT - This is testing program
    OUTPUT - 4
     """
    my_str_list = my_str.split(" ")
    return len(my_str_list)


print(count_words("This is testing program"))
