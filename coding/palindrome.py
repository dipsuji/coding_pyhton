def check_palindrome(n):
    temp = n
    rev = 0
    while n > 0:
        # this give last element
        dig = n % 10
        # make reverse element
        rev = rev * 10 + dig
        print (rev)
        n = n // 10
    if temp == rev:
        print("The number is a palindrome")
    else:
        print("The number is not a palindrome")


check_palindrome(121)


def is_palindrome(string):
    left, right = 0, len(string) - 1
    while right >= left:
        if not string[left] == string[right]:
            return False
        left += 1;
        right -= 1
        return True


print(is_palindrome("aba"))
