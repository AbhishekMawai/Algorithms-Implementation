# Gives list of numbers to be sorted, change filename accordingly.
with open("filename") as f:
    li = []
    for line in f:
        li.append(int(line.strip()))
countinv = 0


def merge(left, right):
    """function for merge procedure, takes O(n) time.
        list,list->list"""
    result = []
    i, j = 0, 0
    # This runs as long as both left and right arrays(lists) have elements
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i = i + 1
        else:
            result.append(right[j])
            j = j + 1
            global countinv  # counter for inversions
            countinv = countinv + len(left[i:])
    while i < len(left):  # To copy all the remaining elements from left array(list) if right one is  empty.
        result.append(left[i])
        i = i + 1
    while j < len(right):  # To copy the remaining elements from right array(list) if left one is empty.
        result.append(right[j])
        j = j + 1
    return result


def mergesort(A):
    """Function for spliting the array(list) into left and right and for recussive calls, this takes O(lg n) steps.
        list->list,list"""
    if len(A) < 2:
        return A[:]
    else:
        middle = len(A) // 2
        left = mergesort(A[:middle])  # Calling recursively to store result returned from merge().
        right = mergesort(A[middle:])  # Calling recursively to store result returned from merge().
        return merge(left, right)
# print("Sorted elements:=",mergesort(li)) #(uncomment if you want to see the sorted result)


mergesort(li)
print("Number of Inversions:", countinv)
