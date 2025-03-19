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

input_from_user()
