def fibi(n):
    a, b = 0, 1
    for i in range(n):
        # fibonacci series is next no. is sum of previous two number.
        temp = a
        a = b
        # now nth fibonacci no. is sum of previous two number.
        b = temp+b
    #  returning a because a changing each places
    return a


result = fibi(0)
print(result)

result = fibi(1)
print(result)

result = fibi(7)
print(result)