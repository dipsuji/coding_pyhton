from collections import Counter


def duplicate_char(st):
    """
     print duplicate character from string
        output
        dictionary: Counter({'a': 3, 'm': 2, 's': 2, 'b': 1, 'e': 1, 'i': 1, 'l': 1, 't': 1, 'y': 1})
        dict_str_count.key: ['a', 'b', 'e', 'i', 'm', 'l', 's', 't', 'y']
        a m s
    """
    # key is character of string and value is count of character in string
    dict_str_count = Counter(st)
    print("dictionary: " + str(dict_str_count))
    print("dict_str_count.key: " + str(dict_str_count.keys()))

    index = 0
    # Finding no. of occurrence of a character and get the index of it.
    for char_frequency in dict_str_count.values():  # [3,2,2....]
        # all the indexes from the keys which have value greater than 1.
        if char_frequency > 1:
            # kes are in alphabetical order
            print dict_str_count.keys()[index],
        # go to next index
        index = index + 1


duplicate_char("malayamisbest")
