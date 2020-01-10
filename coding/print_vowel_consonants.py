def find_vowel_consonant(st):
    """
    print vowel and consonant from string

    output for ABCDeb-
    a - is a Vowel
    b - is a Consonant
    c - is a Consonant
    d - is a Consonant
    e - is a Vowel
    b - is a Consonant

    """

    for i in range(len(st)):
        # making lower case
        st = st.lower()
        ch = st[i]
        if ch.isalpha():  # this is alphanumeric character
            if ch in 'aeiou':
                # we can do following way also
                # or if ch in ('a', 'e', 'i', 'o', 'u'):
                # if ch == 'A' or ch == 'a' or ch == 'E' or ch == 'e' or ch == 'I' or ch == 'i' or ch == 'O' or ch == 'o' or ch == 'U' or ch == 'u':
                print(ch + " - is a Vowel")
            else:
                print(ch + " - is a Consonant")
        else:
            print "Neither vowel nor consonant"


# find_vowel_consonant("")

find_vowel_consonant("ABCDeb")
