def pack(my_str):
    """
    implement the function packed the string
    """
    # Empty list of tuple
    packed_list = []
    str_len = len(my_str)
    count = 1
    for i in range(str_len):
        # Count thr character if current and next character is same
        if i < str_len - 1 and my_str[i] == my_str[i + 1]:
            count = count + 1
        else:
            # if i got current and next char is different then put in tuple as char and count
            packed_list.append((my_str[i], count))
            # now reset the counting
            count = 1

    return packed_list


def decode(packed_list):
    """
    implement the function packed the string
    """
    # Empty list of tuple
    decode_str = ""
    list_len = len(packed_list)
    for i in range(list_len):
        # element of packed list
        str_tuple_count = packed_list[i]
        # find number of counting from tuple
        count = str_tuple_count[1]
        while count:
            # add the character in string for all count
            decode_str = decode_str + str_tuple_count[0]
            count = count - 1

    return decode_str


packed = pack("aaaabbccddeaaa")
print(packed)
print(decode(packed))
