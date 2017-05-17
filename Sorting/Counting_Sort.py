# Update with elements to be sorted or from a file.
List_ = [0, 9, 8, 1, 2, 8, 51, 68, 7, 3]
largest = 68  # Update with largest element in the range of input
temp = [0] * (largest + 1)  # Since lists are 0 indexed.
out = [0] * (len(List_))
for b in range(0, len(List_)):
    temp[List_[b]] = temp[List_[b]] + 1
for c in range(1, largest + 1):
    temp[c] = temp[c] + temp[c - 1]
for d in range(len(List_) - 1, -1, -1):
    # Reduce index by 1 in output(out) list.
    out[temp[List_[d]] - 1] = List_[d]
    temp[List_[d]] -= 1
print(out)
