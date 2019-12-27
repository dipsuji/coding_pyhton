def find_triplets(ar):
    """
    Problem statement-
    https://www.geeksforgeeks.org/find-triplets-array-whose-sum-equal-zero/
    """
    ar_len = len(ar)
    # assume no triplet found
    is_triple_occur = False
    for i in range(0, ar_len - 2):
        for j in range(i + 1, ar_len - 1):
            for k in range(j + 1, ar_len):
                # NOW CHECK FOR sum of all a, b, c
                if ar[i] + ar[j] + ar[k] == 0:
                    print(ar[i], ar[j], ar[k])
                    # now we found at least one triplet
                    is_triple_occur = True
    # If no triplet found with 0 sum then print not exist
    if not is_triple_occur:
        print("Triplet not found ")


# arr = [0, 1, 1, -3, 4]
arr = [-1, 0, 2, -3, 1]

# biogo n3 solution
find_triplets(arr)

"""
Output -
(-1, 0, 1)
(2, -3, 1)
"""
