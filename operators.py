from operator import truediv
from os import chown


def my_function(first_name):
    print(first_name)


# my_function("ori")


def calculate_bmi(weight, height):
    return weight / (height ** 2)


# print(calculate_bmi(70, 1.74))


def perimeter_rectangle(length, height):
    return 2 * (length + height)


def area_rectangle(length, height):
    return length * height


def average(num1, num2, num3, num4, num5):
    sum = num1 + num2 + num3 + num4 + num5
    num_of_parameters = 5
    return sum / num_of_parameters


def final_price(price, discount):
    return (discount * price) / 100


def print_char(char1, char2, char3, char4, char5, char6):
    print(char1 + char2 + char3)
    print(char4 + char5)
    print(char6)


# print_char('m', 'm', 'm', 'm', 'm', 'm')


def calculate_minutes(hour, minute):
    return (hour * 60) + minute


def calculate_minute_day():
    minute = 60
    hour = 24
    return minute * hour


def calculate_second():
    seconds_per_minute = 60
    return seconds_per_minute * calculate_minute_day()


# print(calculate_second())


def calculate_present(days):
    year = 365
    return (days * year) // 100


# a = 3 b = 10 c = 17
def swap(a, b, c):
    temp1 = b
    b = a
    temp2 = c
    c = temp1
    a = temp2
    print(a, b, c)


# swap(10, 17, 3)


def swap_without_temp(a, b, c):
    print(f"before swap {a}")
    print(f"before swap {b}")
    print(f"before swap {c}")
    a = a + b + c
    b = a - (b + c)
    c = a - (b + c)
    a = a - (b + c)
    print(f"after swap {a}")
    print(f"after swap {b}")
    print(f"after swap {c}")


def swap_python(a, b, c):
    print(f"before swap {a}")
    print(f"before swap {b}")
    print(f"before swap {c}")
    a, b, c = c, b, a
    print(f"after swap {a}")
    print(f"after swap {b}")
    print(f"after swap {c}")


# swap_python(1, 2, 3)

def mix_str(chain, num):
    print(int(chain) + num)


# mix_str("3" , 3)

def casting():
    print(bool(False))


# casting()

def input_from_user():
    num1 = input("Enter float number1")
    num2 = input("Enter float number3")
    num3 = input("Enter float number2")
    print(f"{num1 + num2}")
    print(num1 + num3)
    print(num2 + num3)


def boolean():
    num = int(input("Enter one number"))
    if num <= 10 and num <= 20:
        return False
    return True


def paper():
    x = 5
    flag = True
    return (x > 0 and x < 10) or not flag


def paper2():
    y = 3.14
    z = 8
    return y > 3.0 and (z >= 8 or z < 0)


#print(paper2())

def comparing_int():
    num1 = int(input("Enter one number"))
    num2 = int(input("Enter one number"))
    num3 = int(input("Enter one number"))
    if 15 < num1 < 150 and 15 < num2 < 150 and 15 < num3 < 150:
        print("The numbers are in rage")

    if num2 != num1 and num3 != num1:
        print("The numbers are not equal")

    if num1 == num2 or num1 == num3:
        print("The first number is equal")

    if num1 == num2 or num2 != num3:
        print("the second number is ")


#comparing_int()

def comparing_strings1():
    sum1 = sum2 = sum3 = 0
    str1 = input("Enter one string")
    str2 = input("Enter one string")
    str3 = input("Enter one string")

    ascii_value_str1 = [ord(char1) for char1 in str1]
    ascii_value_str2 = [ord(char2) for char2 in str2]
    ascii_value_str3 = [ord(char3) for char3 in str3]

    sum1 = sum(ascii_value_str1)
    sum2 = sum(ascii_value_str2)
    sum3 = sum(ascii_value_str3)

    if 15 < sum1 < 150 and 15 < sum2 < 150 and 15 < sum3 < 150:
        print("The strings are in rage")
    else:
        print("One or more strings are out of range")


#comparing_strings1()

def comparing_strings2():

    str1 = input("Enter one string")
    str2 = input("Enter one string")
    str3 = input("Enter one string")

    if str1 != str3 and str1 != str2:
        print("The strings are not equals")

    if str1 == str2 or str1 == str3:
        print("one or more strings are equals")

    if str2 == str1 or str2 != str3:
        print("the first equals and third not")

#comparing_strings2()

def is_divide(num):
    temp = num
    divider = num % 10
    num //= 10
    new_num = divider + num
    if temp % new_num != 0:
        return False
    return True

#print(is_divide(17))

def from_user():
    num = int(input("Enter number with 7 digits"))
    last = num % 10
    first = num // 1000000
    sixth = (num // last) % 10
    second = (num // 100000) % 10
    fifth = (num // 100) % 10
    forth = (num // 1000) % 10
    third =(num // 10000) % 10



    if last == first:
      print("the first and last equals")
    else:
        print("the first and last are not equals")

    if sixth != second:
        print("the second and the sixth are not equals")
    else:
        print("the second and the sixth are equals")

    if third == forth and third != fifth:
        print("the numbers in the middle are not equals")

#print(from_user())

def bigger_then_middle():
    num1 = int(input("Enter one number"))
    num2 = int(input("Enter one number"))
    num3 = int(input("Enter one number"))

    return (num1 + num3) > num2

#print(bigger_then_middle())

def sum_num(num):
    sum1 = 0
    while(num > 0):
        sum1 += (num % 10)
        num //= 10
    print(sum1)


#sum_num(3504)

def hint():
    a: int = 5
    a = 'avi'
    print(a)

#hint()


def title():
    avi = 0
    print("avi".title())
    print(avi.title())

#title()

def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return True
    elif year % 4 == 0:
        return True
    else:
        print(f"The year {year} is not leap ")