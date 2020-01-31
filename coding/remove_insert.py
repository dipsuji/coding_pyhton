def remove_at(index, my_str):
    """
    Remove character from string from specific index
    """
    # making substring up to given index
    # and substring after given index
    if index < 0 or index >= len(my_str):
        print "invalid index"
        return my_str

    return my_str[:index] + my_str[index + 1:]


def insert_at(index, my_chr, my_str):
    """
    implement the function insert character at given index in the string
    """
    if index < 0 or index > len(my_str):
        print "invalid index"
        return my_str
    # use substring and add given index
    return my_str[:index] + my_chr + my_str[index:]


print(remove_at(0, "abcd"))
print(insert_at(1, 'A', "abcd"))
