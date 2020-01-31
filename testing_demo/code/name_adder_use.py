def formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()


# Failing a test demo -
# To show test fail modify a  formatted_name() function by including a new middle name argument.

def formatted_name1(first_name, middle_name, last_name):
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    return full_name.title()


# for making right test case-
def formatted_name2(first_name, last_name, middle_name=''):
    if len(middle_name) > 0:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()
