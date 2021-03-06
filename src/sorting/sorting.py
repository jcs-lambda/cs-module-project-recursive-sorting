def merge(arrA:list, arrB:list) -> list:
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # length of merged array is sum of passed arrays
    # loop is finished when both arrays are empty
    for i in range(len(merged_arr)):
        # arrA is empty, grab from arrB
        if not arrA:
            merged_arr[i] = arrB.pop(0)
        # arrB is empty, grab from arrA
        elif not arrB:
            merged_arr[i] = arrA.pop(0)
        # next value in arrA is less than next value in arrB
        # grab from arrA
        elif arrA[0] < arrB[0]:
            merged_arr[i] = arrA.pop(0)
        # next value in arrA is greater than or equal to next value in arrB
        # grab from arrB
        else:
            merged_arr[i] = arrB.pop(0)
    
    return merged_arr


def merge_sort(arr):
    # split array into halves
    midpoint = len(arr) // 2
    left = arr[:midpoint]
    right = arr[midpoint:]

    # recurse while working with halves where either's length
    # is greater than 1
    if len(left) > 1 or len(right) > 1:
        return merge(merge_sort(left), merge_sort(right))
    # base case: each half has no more than 1 item
    # begin unwiding recursion
    else:
        return merge(left, right)


# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass

def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
