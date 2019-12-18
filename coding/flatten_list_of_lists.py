# input list
def remove_nesting(nested_list, result1):
    """
    this method will convert nested list to single list
    """
    for item in nested_list:
        if type(item) == list:
            # if element is list type then call same function in recursive fashion
            print("List found do recursive call :" + str(item))
            remove_nesting(item, result1)
        else:
            # add item in result list
            result1.append(item)
            print(result1)


result = []
remove_nesting([1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]], result)

print ('Flatten list of nested list : ', result)

"""
Output

[1]
[1, 2]
List found do recursive call :[3, 4, [5, 6]]
[1, 2, 3]
[1, 2, 3, 4]
List found do recursive call :[5, 6]
[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5, 6]
[1, 2, 3, 4, 5, 6, 7]
[1, 2, 3, 4, 5, 6, 7, 8]
List found do recursive call :[9, [10]]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
List found do recursive call :[10]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
('Flatter list of nested list : ', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
"""
