# input list
def implement_nested_list(nested_list, result1):
    """
    this method make single list of nested list

    sample output

    [1]
    now List found then recursive call :[2, 3]
    [1, 2]
    [1, 2, 3]
    [1, 2, 3, 4]
    [1, 2, 3, 4, 5]
    now List found then recursive call :[6]
    [1, 2, 3, 4, 5, 6]
    output: [1, 2, 3, 4, 5, 6]

    """

    if len(nested_list) == 0:
        return False
    for elements in nested_list:
        if type(elements) == list:
            # if element is type of list then call same function
            print("now List found then recursive call :" + str(elements))
            implement_nested_list(elements, result1)
        else:
            # add item in result list
            result1.append(elements)
            print(result1)


result = []
result1 = implement_nested_list([1, [2, 3], 4, 5, [6]], result)
# result1 = implement_nested_list([], result)

if not result1:
    print(False)
else:
    print('output: ' + str(result))
#