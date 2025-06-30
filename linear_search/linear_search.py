def linear_search_simple(arr, target):
    """
    Performs a simple linear search to find the target in the array.
    Returns the index of the target if found, otherwise returns -1.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def linear_search_bidirectional(arr, target):
    """
    Performs a linear search from both ends of the array to find the target.
    Returns the index of the target if found, otherwise returns -1.
    """
    left = 0
    right = len(arr) - 1
    while left <= right:
        if arr[left] == target:
            return left
        if arr[right] == target:
            return right
        left += 1
        right -= 1
    return -1
