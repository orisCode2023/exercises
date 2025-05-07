user_input = input("Enter number with 5 digits ")


def print_input():
    global user_input
    while len(user_input) != 5 or not user_input.isdigit():
        user_input = input("Enter number with 5 digits ")

    print(f"the input the user put is: {user_input}")
    assert len(user_input) == 5, "Input should be exactly 5 digits"
    assert user_input.isdigit(), "Input should contain only digits"


def using_join_method():
    global user_input
    new_str = ",".join(user_input)
    return new_str


def remove_comma():
    clean_str = using_join_method()
    return clean_str.replace(",", "")


def converting_str_to_list():
    string = remove_comma()
    return list(string)


def converting_list_of_str_to_int():
    new_list = converting_str_to_list()
    integer_lst = [int(item) for item in new_list]
    return integer_lst


def sum_of_list():
    new_list = converting_list_of_str_to_int()
    sum_numbers = 0
    for number in new_list:
        sum_numbers += number
    print(f"the sum of new input is: {sum_numbers}")


print_input()
print(using_join_method())
sum_of_list()

