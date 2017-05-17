# List to be sorted, update accordingly. or use another form of input.
li = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]


def HeapSort(A):
    heap_size = len(A)

    def Max_Heapify(A, i):
        left = (i * 2) + 1
        right = (i * 2) + 2
        if left <= heap_size - 1 and A[left] > A[i]:
            largest = left
        else:
            largest = i
        if right <= heap_size - 1 and A[right] > A[largest]:
            largest = right
        if largest != i:
            A[i], A[largest] = A[largest], A[i]
            Max_Heapify(A, largest)

    def Build_Max_Heap(A):
        for i in range(len(A) // 2, -1, -1):
            Max_Heapify(A, i)
    Build_Max_Heap(li)
    for i in range(len(A) - 1, -1, -1):
        A[0], A[i] = A[i], A[0]
        heap_size = heap_size - 1
        Max_Heapify(A, 0)


HeapSort(li)
print("Sorted List=", li)
