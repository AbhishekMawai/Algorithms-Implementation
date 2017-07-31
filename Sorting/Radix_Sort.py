li = [170, 45, 75, 90, 802, 24, 2, 69, 66]


def countingsort(li, exp):
    temp = [0] * 10
    out = [0] * len(li)
    for b in range(0, len(li)):
        ind = (li[b] // exp) % 10
        temp[ind] = temp[ind] + 1

    for c in range(1, 10):
        temp[c] = temp[c] + temp[c - 1]

    for d in range(len(li) - 1, -1, -1):
        ind = (li[d] // exp) % 10
        out[temp[ind] - 1] = li[d]
        temp[ind] -= 1
    for i in range(len(li)):
        li[i] = out[i]


def radixsort(li):
    max1 = max(li)
    exp = 1
    while max1 // exp > 0:
        countingsort(li, exp)
        exp *= 10
    print(li)


radixsort(li)
