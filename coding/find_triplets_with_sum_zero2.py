
def find_triplets_with_sum_zero(arr):
    """
    this solution with bigo n2
    Problem statement-
    https://www.geeksforgeeks.org/find-triplets-array-whose-sum-equal-zero/
    """
    n = len(arr)
    is_triple_occur = False
    # sort array elements
    arr.sort()
    print(arr)
    for i in range(0, n - 1):
        # initialize left and right
        l = i + 1
        r = n - 1
        x = arr[i]
        while l < r:
            print("")
            print("Left " + str(arr[l]))
            print("Right " + str(arr[r]))
            print("Current item " + str(x))
            if x + arr[l] + arr[r] == 0:
                print("Sum is zero now-- Triplet-----")
                # print elements if it's sum is zero
                print(x, arr[l], arr[r])
                l += 1
                r -= 1
                is_triple_occur = True

            # If sum of three elements is less than zero then increment in left
            elif x + arr[l] + arr[r] < 0:
                print("Increase left pointer")
                l += 1

            else:
                # If sum of three elements is grater than zero then decrement in right
                print("Decrease right pointer")
                r -= 1

    if not is_triple_occur:
        print("Triplet not found ")


arr = [0, -1, 2, -3, 1]
find_triplets_with_sum_zero(arr)

"""
Output - 
[-3, -1, 0, 1, 2]

Left -1
Right 2
Current item -3
Increase left pointer

Left 0
Right 2
Current item -3
Increase left pointer

Left 1
Right 2
Current item -3
Sum is zero now-- Triplet-----
(-3, 1, 2)

Left 0
Right 2
Current item -1
Decrease right pointer

Left 0
Right 1
Current item -1
Sum is zero now-- Triplet-----
(-1, 0, 1)

Left 1
Right 2
Current item 0
Decrease right pointer
"""
