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
    # Your code here
    pass
