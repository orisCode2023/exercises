def print_pair():
    nums = [1, 2, 4, 5, 6, 7]
    result = []
    for num in nums:
        if num % 2 == 0:
            result.append(num // 2)

    print(result)


def print_times_5():
    for i in range(1, 6):
        print(f"{i} " * 5)


# print_times_5()
def print_arrow_with_2_loops():
    for i in range(1, 6):
        print("* " * i)

    for j in range(4, 0, -1):
        print("* " * j)


def print_arrow_with_one_loop():
    astric = 0
    for i in range(1, 10):
        if i <= 5:
            astric = i
        else:
            astric -= 1

        print("* " * astric)

#print_arrow_with_one_loop()

def print_piramida():
    num_rows = 4
    for i in range(1, 5):
        numbers = (str(i) + " ") * i
        space = " " * (num_rows - i)
        print(space + numbers)

# print_piramida()


