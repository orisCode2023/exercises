def print_by_input():
    lst = []
    number1 = int(input("enter number"))
    lst.append(number1)
    number2 = int(input("enter number"))
    lst.append(number2)
    number3 = int(input("enter number"))
    lst.append(number3)
    number4 = int(input("enter number"))
    lst.append(number4)
    number5 = int(input("enter number"))
    lst.append(number5)
    number6 = int(input("enter number"))
    lst.append(number6)

    press = input("press somthing")
    print(lst[0])
    press1 = input("press somthing")
    print(lst[1])
    press2 = input("press somthing")
    print(lst[2])
    press3 = input("press somthing")
    print(lst[3])
    press4 = input("press somthing")
    print(lst[4])
    press5 = input("press somthing")
    print(lst[5])

def print_even():
    lst = []
    number1 = int(input("enter number"))
    lst.append(number1)
    number2 = int(input("enter number"))
    lst.append(number2)
    number3 = int(input("enter number"))
    lst.append(number3)
    number4 = int(input("enter number"))
    lst.append(number4)
    number5 = int(input("enter number"))
    lst.append(number5)
    number6 = int(input("enter number"))
    lst.append(number6)

def pop():
    lst = [1, 2, 3]
    while len(lst) != 0:
        num = lst.pop(0)
        print(num)

pop()
