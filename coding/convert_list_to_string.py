"""
convert a list to string
"""


def list_to_string(ls):
    # now initialize an empty string
    str1 = ""
    for element in ls:
        # print(element)
        str1 += element

    return str1


ls = ['Python', 'Programming', 'Practice']
print(list_to_string(ls))
