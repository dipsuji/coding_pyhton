def count_occurrence_word(my_str, word):
    # split the string into words by spaces in word_list list
    word_list = my_str.split(" ")
    print word_list
    count = 0
    # # search the word in list word_list
    for i in range(0, len(word_list)):
        # if word found then increase count
        if word == word_list[i]:
            count = count + 1

    return count


print count_occurrence_word("This is my lovely book", "my")
