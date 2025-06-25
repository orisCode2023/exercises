from create_map_from_scratch import my_list


def print_sentence():
    print("Hello World")


def combine_string(str1, str2, str3):
    return str1 + " " + str2 + " " + str3


# print(combine_string("hi", "to" , "world"))


def revers_str(string):
    return string[:: -1]


def is_palindrome(string):
    return string == string[::-1]


def sum_of_num(num):
    total = 0
    for i in range(num):
        total += i
    return total


def sum_of_list(lst):
    total = 0
    for number in lst:
        total += number
    return total


def print_stars_in_revers(lst=[]):
    lst.reverse()
    lst2 = []
    for number in lst:
        lst2.append(number * "*")

    return lst2


# print(print_stars_in_revers([1, 3, 5]))


def sum_numbers(num1, num2):
    return num1 + num2


def multiple_numbers(num1, num2):
    return num1 * num2


def list_of_cal(number):
    lst = []
    lst.append(multiple_numbers(number, number + 1))
    lst.append(sum_numbers(number, number + 1))
    lst.append(multiple_numbers(number, number - 1))
    lst.append(sum_numbers(number, number - 1))
    return lst


# print(list_of_cal(5))

def return_sum_unknown_numbers(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total


def return_pair_list(*numbers):
    lst = []
    for index, number in enumerate(numbers):
        if number % 2 == 0:
            lst.append(index)

    return lst


def return_dictionary(**kwargs):
    return kwargs
