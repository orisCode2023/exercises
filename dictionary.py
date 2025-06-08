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
    dic1 = {True: [1,2,3],
            False: [1,2,3]}
    print(dic1)
    dic2 = {{1, 2}: 234}
    print(dic2)

#testing_dictionary()

def print_collections(idx):
    if idx == 5:
        return
    names_list = ["gad", "ben", "dan", "ori", "david"]
    birth_year = (2001, 2002, 2003, 2004, 2005)
    birth_country = ("Israel", "German", "France", "Spain", "New York")

    print(f" The name is: {names_list[idx]}, and he was born in {birth_year[idx]}, in {birth_country[idx]} ")
    print_collections(idx + 1)

#print_collections(0)

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

#converting()

def update_dic_price():
    cart = {"rice": 15, "pasta": 50, "flower": 7}
    cart["rice"] += 10
    cart["pasta"] -= 30

    print(cart)
#update_dic_price()

