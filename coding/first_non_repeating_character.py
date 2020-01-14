def first_non_repeat_char(my_str):
    # making a array
    char_array = []
    # making a list
    char_list = {}
    for ch in my_str:
        #  check character in ctr_dic
        if ch in char_list:
            # if char already in char_list then increase counting but in intial there are no any element
            char_list[ch] += 1
        else:
            # if char not in ctr_dic then put its counting as 1
            char_list[ch] = 1
            # and that character apend in array
            char_array.append(ch)
            # print char_array
    for ch in char_array:
        # check counting of char from array in char_list is 1
        if char_list[ch] == 1:
            return ch
    return None


print first_non_repeat_char("ssuumed")
# print first_non_repeat_char("abghss")
# print first_non_repeat_char("aabbcc")
