import random
from pprint import pprint


def input_till_0():
    arr = []
    num = 1
    last = 0
    while num != 0:
        num = int(input("Enter number "))
        if num != 0:
            arr.append(num)

    print(arr)
    last = arr.pop()
    arr.insert(0, last)
    print(arr)


# input_till_0()

def check_in_matrix():
    lst = [[5, 4, 3],
           [1, 10, -5],
           [10, 30, 15, 2],
           [200, 20]]
    if len(lst) != 4:
        return
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            num = random.randint(-10, 300)
            current = lst[i][j]
            if current == num:
                print(i, j)
            else:
                print("not in the list")


# check_in_matrix()

def print_table_100():
    for i in range(1, 11):
        for j in range(1, 11):
            print(i * j, end=" ")
        print()


# print_table_100()
def create_and_fill_matrix_from_input():
    input = 5
    rows = input
    col = input
    matrix = []
    i = 1
    size = pow(input, 2)
    for _ in range(rows):
        row = []
        for _ in range(col):
            if i <= size:
                row.append(i)
            i += 1
        matrix.append(row)

    print(matrix)


# create_and_fill_matrix_from_input()
def practice_matrix():
    matrix = []
    rows = col = 4
    new_matrix = []
    total = max = idx = 0
    counter = rows * col
    dic = {}
    for _ in range(rows):
        row = []
        row_new_matrix = []
        for j in range(col):
            num = random.randint(0, 100)
            total += num
            row.append(num)
            if j % 2 == 0:
                row_new_matrix.append(row[j])

            if num in dic:
                dic[num] += 1
            else:
                dic.update({num: 1})

        matrix.append(row)
        new_matrix.append(row_new_matrix)
    for l, k in dic.items():
        if k > max:
            max = k
            idx = l
    print(f"the pair matrix is {new_matrix}")
    average = total // counter
    print(matrix)
    print(f" the sum is: {total}")
    print(f"the average is: {average}")
    print(f"the value that exist the most is {idx}")


# practice_matrix()

def sum_of_matrix():
    rows = col = 4
    matrix = []
    sum_diagonals = back_sum_diagonals = sum_first_col = sum_last_col = sum_frame = top_row = bottom_row = 0
    for i in range(rows):
        row = []
        for j in range(col):
            num = random.randint(0, 100)
            row.append(num)
            if i == j:
                sum_diagonals += row[j]
            if i + j == col - 1:
                back_sum_diagonals += row[j]
            if j == 0:
                sum_first_col += row[j]
            if j == rows - 1:
                sum_last_col += row[j]
            if i == 0:
                if 0 < j < rows - 1:
                    top_row += row[j]
            if i == rows - 1:
                if 0 < j < rows - 1:
                    bottom_row += row[j]

        matrix.append(row)
    sum_frame = sum_first_col + sum_last_col + top_row + bottom_row
    print(f"The matrix is: {matrix}")
    print(f"The sum of the diagonals is: {sum_diagonals}")
    print(f"The sum of the back diagonals is: {back_sum_diagonals}")
    print(f"The sum of the first col is: {sum_first_col}")
    print(f"The sum of the last col is: {sum_last_col}")
    print(f"The sum of the top row is: {top_row}")
    print(f"The sum of the last row is: {bottom_row}")
    print(f"The sum of the matrix frame is: {sum_frame}")


# sum_of_matrix()

def rotate_matrix():
    rows = col = 4
    matrix = [[1, 1, 1, 1, 1],
              [2, 2, 2, 2, 2],
              [3, 3, 3, 3, 3],
              [4, 4, 4, 4, 4],
              [5, 5, 5, 5, 5]]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i == 0:
                matrix[i][j], matrix[col][rows] = matrix[col][rows], matrix[i][j]
                col -= 1
                rows -=1
                if j == len(matrix) - 2:
                    break

    pprint(matrix)


# rotate_matrix()


def rotate_matrix_dinamy():
    matrix = [[]]
    rows = col = len(matrix) - 1
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i == 0:
                matrix[i][j], matrix[col][rows] = matrix[col][rows], matrix[i][j]
                col -= 1
                if j == len(matrix) - 2:
                    break

    pprint(matrix)


# rotate_matrix()


def check_sub_matrix():
    matrix = [[1, 1, 1, 1, 1],
              [2, 2, 2, 2, 2],
              [3, 3, 3, 3, 3],
              [4, 4, 4, 4, 4],
              [5, 5, 5, 5, 5]]
    sub_matrix = [[2,2]]

#     for i in range(len(matrix)):
#         for j in range(len(matrix)):
#
#
# print(check_sub_matrix())

def tuple_to_matrix():
    print()
#tuple_to_matrix()

def is_palindrome():
    num = 121
    original = num
    new_num = 0
    while num != 0:
        temp = (num % 10)
        new_num *= 10
        new_num += temp
        num //= 10

    if original != new_num:
        return False

    return True

# print(is_palindrome())
def rotate_all_mat():
    matrix = [[1, 1, 1, 1, 1],
              [2, 2, 2, 2, 2],
              [3, 3, 3, 3, 3],
              [4, 4, 4, 4, 4],
              [5, 5, 5, 5, 5]]
    rows = col = len(matrix)
    for i in range(len(matrix)):
        col -= 1
        for j in range(len(matrix)):
            rows -= 1
            matrix[i][j], matrix[col][rows] = matrix[col][rows], matrix[i][j]
            if j == col:
                break
    pprint(matrix)

# rotate_all_mat()
from pprint import pprint


def rotate_matrix_90_clockwise():
    matrix = [[1, 1, 1, 1, 1],
              [2, 2, 2, 2, 2],
              [3, 3, 3, 3, 3],
              [4, 4, 4, 4, 4],
              [5, 5, 5, 5, 5]]

    n = len(matrix)

    # Rotate layer by layer from outside to inside
    for layer in range(n // 2):
        first = layer
        last = n - 1 - layer

        for i in range(first, last):
            offset = i - first

            # Save top element
            top = matrix[first][i]

            # Top = Left
            matrix[first][i] = matrix[last - offset][first]

            # Left = Bottom
            matrix[last - offset][first] = matrix[last][last - offset]

            # Bottom = Right
            matrix[last][last - offset] = matrix[i][last]

            # Right = Top
            matrix[i][last] = top

    pprint(matrix)


#rotate_matrix_90_clockwise()

def merge():
    arr = []
    nums1 = [1, 2, 3]
    nums2 = [2, 5, 6]
    idx1 = idx2 = 0
    n = len(nums2)
    m = len(nums1) + n

    for _ in range(m):

        if idx1 < len(nums1) and nums1[idx1] < nums2[idx2]:
            arr.append(nums1[idx1])
            idx1 += 1
        elif idx2 < len(nums2):
            arr.append(nums2[idx2])
            idx2 += 1

    nums1 = arr

    return nums1

# print(merge())

def print_10_on_10():
    matrix = []
    for i in range (10):
        matrix.append([])
        for j in range(10):
            matrix[i].append((i + 1) * (j + 1))

    pprint(matrix)

# print_10_on_10()
def test():
    nums = [2,2,1,1,1,2,2]
    dic = {}
    temp = 0
    for num in nums:
        if num in dic:
            dic[num] += 1
        else:
            dic.update({num: 1})
    for key, value in dic.items():
        if value > len(nums) / 2:
            temp = key
    return temp

print(test())










