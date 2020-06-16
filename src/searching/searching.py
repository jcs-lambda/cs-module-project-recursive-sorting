# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    found = -1

    if start <= end:
        center = (start + end) // 2
        if arr[center] == target:
            found = center
        elif arr[center] < target:
            return binary_search(arr, target, center + 1, end)
        else:
            return binary_search(arr, target, start, center - 1)
    
    return found

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # markers for each end of range that can contain the target
    lowest_index, highest_index = 0, len(arr) - 1
    # index of target in arr (-1 is not found)
    found = -1

    # check for ascending / descending, grab appropriate comparison operator
    if arr[0] < arr[1]: # ascending
        compare = target.__le__
    else: # descending
        compare = target.__gt__

    # loop until target found or list exhausted
    while lowest_index <= highest_index and found < 0:
        # marker for center of range that can contain target
        center_index = (lowest_index + highest_index) // 2

        # current center equals target, update found index
        if arr[center_index] == target:
            found = center_index
        # use apprpriate comparison based on ascending or descending order,
        # if True, target is to the left of center_index,
        # adjust highest_index to one less than current center_index
        elif compare(arr[center_index]):
            highest_index = center_index - 1
        # target is to the right of center_index,
        # adjust lowest_index to one more than current center_index
        else:
            lowest_index = center_index + 1

    return found