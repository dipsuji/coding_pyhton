"""
convert a list to string using join() function
"""


def listToString(ls):
    # here we initialize an empty string
    str1 = " "
    return str1.join(ls)


ls = ['Python', 'Programming', 'Practice']
print(listToString(ls))
