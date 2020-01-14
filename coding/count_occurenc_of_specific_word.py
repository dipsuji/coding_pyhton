def count_occurrence_word(my_str, word):
    """
    Count the occurrence of specific word in string

    Input-
    This is my lovely book, my father given me, my
    Output-
    2
    """
    # split the string into words by spaces in word_list list
    # bigo n time
    word_list = my_str.split(" ")
    print word_list
    count = 0
    # # search the word in list word_list
    for i in range(0, len(word_list)):
        # if word found then increase count
        if word == word_list[i]:
            count = count + 1

    return count


print count_occurrence_word("This is my lovely book, my father given me", "my")