def first_non_repeat_char(my_str):
    """
    Print first non repeating character of String
    INPUT - ssuumed
    OUTPUT - m
    """
    # making a empty array
    used_letter_array = []
    # making a dictionary, key is string char and value is occurrence of char
    char_dict = {}
    for ch in my_str:
        #  check character in ctr_dic
        if ch in char_dict:
            # if char already in char_dict then increase counting but in intial there are no any element
            char_dict[ch] += 1
        else:
            # if char not in ctr_dic then put its counting as 1
            char_dict[ch] = 1
            # and that character append in array
            used_letter_array.append(ch)
            # print used_letter_array
    print(char_dict)
    print(used_letter_array)
    # now finding the first non repeating char in used_letter_array
    for ch in used_letter_array:
        # check counting of char from array in char_dict is 1
        if char_dict[ch] == 1:
            return ch
    return None


print(first_non_repeat_char("ssuumed"))
# print first_non_repeat_char("abghss")
# print first_non_repeat_char("aabbcc")
