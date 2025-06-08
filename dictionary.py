def testing_set():
    bool_set = {True, False, True}
    float_set = {1.5, 4.6, 44.6}
    int_set = {1, 2, 3}
    print(bool_set)
    print(float_set)
    int_set.add(4)
    int_set.add(2)
    print(int_set)


# testing_set()

def testing_dictionary():
    dic1 = {True: [1, 2, 3],
            False: [1, 2, 3]}
    print(dic1)
    dic2 = {{1, 2}: 234}
    print(dic2)


# testing_dictionary()

def print_collections(idx):
    if idx == 5:
        return
    names_list = ["gad", "ben", "dan", "ori", "david"]
    birth_year = (2001, 2002, 2003, 2004, 2005)
    birth_country = ("Israel", "German", "France", "Spain", "New York")

    print(f" The name is: {names_list[idx]}, and he was born in {birth_year[idx]}, in {birth_country[idx]} ")
    print_collections(idx + 1)


# print_collections(0)

def converting():
    list1 = []
    list2 = []
    list3 = []
    string1 = ""
    string2 = ""
    string3 = ""
    tuple1 = ()
    tuple2 = ()
    tuple3 = ()
    set1 = {}
    set2 = {}
    set3 = {}

    list1 = tuple(list1)
    list2 = str(list2)
    list3 = set(list3)
    print(f" the list is {list1}")
    print(f" the list is {list2}")
    print(f" the list is {list3}")

    tuple1 = str(tuple1)
    print(f" the tuple is {tuple1}")
    print(f" the tuple is {list(tuple2)}")
    print(f" the tuple is {set(tuple3)}")

    print(f"the string is{list(string1)}")
    print(f"the string is{tuple(string2)}")
    print(f"the string is{set(string3)}")

    print(f"the set is {list(set1)}")
    print(f"the set is {str(set2)}")
    print(f"the set is {tuple(set3)}")


# converting()

def update_dic_price():
    cart = {"rice": 15, "pasta": 50, "flower": 7}
    cart["rice"] += 10
    cart["pasta"] -= 30

    print(cart)


# update_dic_price()
def print_value_counter_dict():
    dic = {}
    string = input("Enter string ")
    for char in string:
        if char in dic.keys():
            dic[char] += 1
        else:
            dic.update({char: 1})
    print(dic)


# print_value_counter_dict()

def switch_key_value():
    dic = {1: "one", 2: "two"}
    new_dic = {}
    for key, value in dic.items():
        new_dic.update({value: key})
    print(new_dic)


# switch_key_value()
def nested_dict():
    key_minimum = None
    key_maximum = None
    key_minimum_for_all = None
    key_maximum_for_all = 0
    minimum_for_all = None
    maximum_for_all = 0
    total = 0
    dic = {"first_dict": {"a": 1, "b": 10},
           "second_dict": {"c": 1000, "d": -500, "e": 0},
           "third_dict": {"f": 200}}
    for i in dic:
        maximum = 0
        minimum = None
        for idx, j in dic[i].items():
            if j > maximum:
                maximum = j
                key_maximum = idx
            if minimum is None or minimum > j:
                minimum = j
                key_minimum = idx
            total += j
            if j > maximum_for_all:
                maximum_for_all = j
                key_maximum_for_all = idx
            if minimum_for_all is None or minimum_for_all > j:
                minimum_for_all = j
                key_minimum_for_all = idx

        print(f"the maximum value in key {key_maximum}: is {maximum}")
        print(f"the minimum value in key {key_minimum}: is {minimum}")
    print(f"the sum of the values is {total}")
    print(f"the maximum value in all dic in key {key_maximum_for_all}: is {maximum_for_all}")
    print(f"the minimum value in all dic in key {key_minimum_for_all}: is {minimum_for_all}")


# nested_dict()

def insert_int_to_dic():
    number = int(input("Enter number "))
    dic = {}
    while number != 0:
        num = number % 10
        number //= 10
        if num in dic:
            dic[num] += 1
        else:
            dic.update({num: 1})
    print(dic)


# insert_int_to_dic()
def dict_with_symbols():
    string = "i want to go 1 2 3 4 5 6 7 8 9 ! @ # $ % ^ & * "
    dic = {}

    print(dic)


dict_with_symbols()
