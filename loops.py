def my_name():
    name = "ori"
    i = 0
    while i < 1000:
        print(f"{name} {i}")
        i += 1


# my_name()

def print_name():
    name = input("Enter your name")
    for i in range(101):
        print(f"{name}: {i}")


# print_name()

def pair_3():
    for i in range(101):
        if i % 3 == 0:
            print(i)


# pair_3()

def pair_3_and_5():
    for i in range(1001):
        if i % 3 == 0 and i % 5 == 0:
            print(i)


# pair_3_and_5()

def divide_by_7_or_9_try_1():
    i = 0
    while i <= 100:
        if i % 9 == 0 and i % 7 == 0:
            print(f"{i}: divide by 9 and 7 ")
        elif i % 9 == 0:
            print(f"{i}: divide by 9")
        elif i % 7 == 0:
            print(f"{i}: divide by 7")
        i += 1


# divide_by_7_or_9_try_1()

def sum_input():
    sum = 0
    while True:
        num = int(input("Enter numer"))
        sum += num
        if num == 0:
            break
    print(sum)


# sum_input()

def boom_7():
    for i in range(1001):
        if i % 7 == 0:
            print("BOOM")
        else:
            print(i)


# boom_7()


def print_count_try_2():
    counter = 0
    num = 0
    while num != -1:
        num = int(input("Enter number "))
        counter += 1
    print(counter)


# print_count_try_2()

def negative_number():
    num = int(input("Enter number < 0 "))
    for i in range(num, 0):
        print(i)


# negative_number()

def print_5_of_5():
    for i in range(5):
        for j in range(5):
            print(i, end="")
        print()


# print_5_of_5()

def divide_by_5_and_3():
    for i in range(1000):
        if i % 5 == 0 and i % 3 == 0:
            print(f"{i}: FuzzBuzz")
        elif i % 5 == 0:
            print(f"{i}: Buzz")
        elif i % 3 == 0:
            print(f"{i}: Fuzz")


# divide_by_5_and_3()

def exit_condition():
    counter = counter_pair = counter_unpair = sum = max = 0
    min = None
    while True:
        condition = input("Do you want to exit write Exit else press Enter")
        if condition == " Exit":
            if counter == 0:
                print("You did not insert any number pleas continue")
                continue
            else:
                print(f"The number of numbers you insert is: {counter}")
                print(f"The number of pairs numbers you insert is: {counter_pair}")
                print(f"The number of unpair numbers you insert is: {counter_unpair}")
                print(f"The greatest number you  insert is: {max}")
                print(f"The smallest number you insert is: {min}")
                print(f"The sum of the numbers you insert is: {sum}")
                print(f"The average of the numbers you insert is: {sum / counter}")
                break

        numbers = int(input("Enter number"))
        counter += 1
        sum += numbers

        if numbers % 2 == 0:
            counter_pair += 1
        else:
            counter_unpair += 1

        if numbers > max:
            max = numbers
        if numbers < min or min == None:
            min = numbers


# exit_condition()

def system():
    counter = 0
    user1 = "123456789"
    # user2 = "987654321"
    # user3 = "012345678"
    password1 = "0507777777"
    # password2 = "0526666666"
    # password3 = "0545555555"
    while True:
        choice = int(input("To enter the system press 1 \n"
                           "To create new user press 2 \n "
                           "To exit the system press 3 "))

        if choice == 1:
            user = str(input("Enter user (the user name should be id)"))
            if not len(user) == 8 or not user.isdigit():
                print("User not found")
            if user == user1:
                print("User found")
                password = str(input("Enter password(the password should be phone number)"))
                if not len(password) == 9 or not password.isdigit():
                    counter += 1
                    print("Wrong Password")
                    if counter == 3:
                        print("Lock Down")
                        break
                if password == password1:
                    print("correct password \n "
                          "WELCOME TO OUR SYSTEM")

                    choice2 = int(input("To change password press 1 \n"
                                        "To delete user press 2 \n"
                                        "To go back to menu press 3 \n"
                                        "To leave the system press 4 "))
                    if choice2 == 1:
                        new_password = str(input("Enter new password"))
                        password = new_password
                    if choice2 == 2:
                        user = None
                    if choice2 == 3:
                        int(input("To enter the system press 1 \n"
                                  "To create new user press 2 \n "
                                  "To exit the system press 3 "))
                    if choice2 == 4:
                        break
            back = str(input("Enter * to go back to menu"))
            if back == "*":
                int(input("To enter the system press 1 \n"
                          "To create new user press 2 \n "
                          "To exit the system press 3 "))

        if choice == 2:
            for i in range(3):
                new_user = str(input("Enter new user(id)"))
                new_password1 = str(input("Enter new password(phone number)"))
                back_to_menu = int(input("To exit the system press 3 "))
        if choice == 3:
            print("Goodbye")
            break


# system()


def print_stars():
    num = int(input("Enter number "))
    number = num * 2 - 1
    for i in range(number):
        if i < num:
            print("*" * (i + 1))
        else:
            print("*" * (number - i))


# print_stars()

def fibonacci():
    num = int(input("Enter number"))
    a, b = 0, 1
    for _ in range(num + 1):
        print(a, end=" ")
        a, b = b, a + b


# fibonacci()

def is_prime():
    num = int(input("Enter number"))
    if num < 2:
        print("is not prime")
        return False
    for i in range(2, int(num ** 0.5 + 1)):
        if num % i == 0:
            print("is not prime")
            return False
    print("is  prime")
    return True


# is_prime()


def up_series():
    i = 0.0
    while i <= 5.0:
        if i.is_integer():
            print(int(i) ,"\n")
        else:
            print(round(i , 1) , end= " ")
        i += 0.1


#up_series()
def string_methods():
    """getting the methods of the string """
    massage = "string"
    print(dir(massage))
#string_methods()

#help(string_methods())

def count_binary():
    num = 101101010101
    counter = 0
    sum_numbers = 0
    while num > 0:
        last = num % 10

        if last == 1:
            sum_numbers += 2 ** counter
        counter += 1
        num //= 10

    print(sum_numbers)

count_binary()

