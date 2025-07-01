def bubble_sort(arr):
    for i in range(len(arr) - 1):
        swapped = False

        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

    return arr

lst = [3, 2, 4, 0, 7, 4, 5, 3, 3]
print(bubble_sort(lst))

