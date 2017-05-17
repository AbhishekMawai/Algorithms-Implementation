li = [2,5,7,3,1,4,9,8,6] # List of numbers to be sorted, change accordingly or for user input if needed.


def merge(left, right):  # function for merge procedure, takes O(n) time.
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):  # This runs as long as both left and right arrays(lists) have elements
        if left[i] < right[j]:
            result.append(left[i])
            i = i + 1
        else:
            result.append(right[j])
            j = j + 1
    while i < len(left):  # To copy all the remaining elements from left array(list) if right one is empty.
        result.append(left[i])
        i = i + 1
    while j < len(right):  # To copy all the remaining elements from right array(list) if left one is empty.
        result.append(right[j])
        j = j + 1
    return result


def mergesort(A):  # Function for spliting the array(list) into left and right and for recussive calls, this takes O(lg n) steps.
    if len(A) < 2:
        return A[:]
    else:
        middle = len(A) // 2
        left = mergesort(A[:middle])  # Calling recursively to get just the leftmost(one) element of returned vale from merge fucntion above.
        right = mergesort(A[middle:])  # Calling recursively to get just the rightmost(one) element of returned vale from merge fucntion above.
        return merge(left, right)


print(mergesort(li))
