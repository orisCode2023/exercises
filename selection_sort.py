array = [100, 54, 85, 90, 51]


def find_min(arr, idx):
    minimum = idx
    for i in range(idx, len(arr)):
        if arr[i] < arr[minimum]:
            minimum = i

    return minimum


def swap(arr, idx1, idx2):
    arr[idx1], arr[idx2] = arr[idx2], arr[idx1]
    return arr


def selection(arr):
    for i in range(len(arr)):
        arr = swap(arr, find_min(arr, i), i)

    return arr


print(selection(array))
