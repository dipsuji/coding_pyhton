def is_polindrome(arr):
    last_index = len(arr) - 1
    for i in range(0, len(arr) / 2):
        if arr[i] != arr[last_index]:
            return False
        last_index = last_index - 1
    return True


print(is_polindrome([3]))
print(is_polindrome([1, 2, 2, 1]))
print(is_polindrome([1, 2, 3, 2, 1]))
print(is_polindrome([2, 2, 3, 2, 1]))
