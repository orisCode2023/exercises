def print_length():
    grades = []
    print(len(grades))
    grades.append(1)
    grades.append(2)
    print(len(grades))

#print_length()


def print_and_change_student():
    students = []
    students.append("ori")
    students.append("david")
    students.append("mark")
    students.append("aviel")
    print(students[1])
    students[1] = "ari"
    print(students)


#print_and_change_student()

def input_and_insert():
    numbers = []
    for i in range(5):
        num = int(input("Enter number "))
        numbers.insert(i , num)

    print(numbers)
    print(len(numbers))


#input_and_insert()

def print_list_items(numbers):
    for i in range(3):
        numbers.insert(i , int(input("Enter number ")))

    for j in numbers:
        print(j)


list= []
#print_list_items(list)

def swap(numbers):
    for i in range(5):
        numbers.insert(i , int(input("Enter number ")))

    numbers[3] , numbers[2] = numbers[2] , numbers[3]
    print(numbers)

#swap(list)

def print_revers_shortest(numbers):
    print(numbers[range(99 , -1 ,-1)])

#print_revers_shortest(list)

def split_to_2_arr(numbers):
    numbers_even = []
    numbers_odd = []
    for i in range(7):
        numbers.append(i)
    print(f"The numbers list is {numbers}")

    for num in numbers:
        if num % 2 == 0:
            numbers_even.append(num)
        else:
            numbers_odd.append(num)

    print(f"The odd list is {numbers_odd}")
    print(f"The even list is {numbers_even}")

#split_to_2_arr([])

def print_is_exist_and_index():
    lst = [5 , 10 , 15 , 20 , 25 , 30]

    number = int(input("Enter number "))
    if number in lst:
        print("is exist")
        x = lst.index(number)
        print(f"the index of the number is {x}")
        if lst[x + 1] != None:
            print(f"The number after our index is {lst[x + 1]}")
        if lst[x - 1] != None:
            print(f"The number before our index is {lst[x - 1]}")
    else:
        print("is not exist")


#print_is_exist_and_index()

def max_input():
    max_number = None
    lst = []
    for i in range(5):
       number = int(input("Enter number "))
       lst.append(number)
       if max_number is None or max_number < number:
           max_number = number

    print(f"the greater number is {max_number} ")

#max_input()

def sort_list():
    lst = []
    sum_numbers = 0
    for i in range(5):
        number = int(input("Enter number "))
        lst.append(number)

    for num in lst:
        if lst.sort() == True:
            sum_numbers += num
            print(f"the sum of the list is {sum_numbers}")
        else:
            sum_numbers += num
            avg = sum_numbers // len(lst)
            print(f"the average of the list is {avg}")

#sort_list()

def sort():
    lst = [1,2,4,5,6,-1]
    lst.sort()
    print(lst)
sort()

