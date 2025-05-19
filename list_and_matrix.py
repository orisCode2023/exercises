def exercise1():
    a = [1, 4, 0, 2, 8]
    print(a[3])
    print(a[3:])
    print(a[:: -1])
    a.insert(0, 5)
    print(a)
    a.pop(len(a) - 1)
    print(a)
    flag = False
    if 0 in a:
        flag = True
    print(flag)
    idx = a.index(0)
    print(idx)

# exercise1()

def exercise2():
    b = [1, 4, 0]
    c = [4, 0, 3]
    d = [8, 2, 0]
    matrix = [b, c, d]
    print(matrix[2][1])
    matrix2 = [[1, 4, 0], [4, 0, 3], [8, 2, 0]]
    print(matrix2[2][1])


#exercise2()

def exercise3():
    matrix = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]]
    print(len(matrix))
    print(len(matrix[0]))
    print(len(matrix) * len(matrix[0]))
    print(matrix[0][::-1])
    print(matrix[1][::-1])
    print(matrix[2][::-1])
    print(matrix[3][::-1])
    matrix[0], matrix[1], matrix[2], matrix[3] = matrix[3], matrix[2], matrix[1], matrix[0]
    print(matrix)




#xercise3()

def exercise4():
    lst = []
    number1 = int(input("enter number "))
    lst.append(number1)
    number2 = int(input("enter number "))
    lst.append(number2)
    number3 = int(input("enter number "))
    lst.append(number3)
    number4 = int(input("enter number "))
    lst.append(number4)
    number5 = int(input("enter number "))
    lst.append(number5)
    number6 = int(input("enter number "))
    lst.append(number6)

    idx = 0
    press = input("press somthing ")
    if idx == len(lst):
        print("goodbye")
    elif press:
        if lst[idx] % 2 == 0:
            print(lst[idx])
        idx += 1

    press = input("press somthing ")
    if idx == len(lst):
        print("goodbye")
    elif press:
        if lst[idx] % 2 == 0:
            print(lst[idx])
        idx += 1

    press = input("press somthing ")
    if idx == len(lst):
        print("goodbye")
    elif press:
        if lst[idx] % 2 == 0:
            print(lst[idx])
        idx += 1

    press = input("press somthing ")
    if idx == len(lst):
        print("goodbye")
    elif press:
        if lst[idx] % 2 == 0:
            print(lst[idx])
        idx += 1

#exercise4()

numbers = []
numbers.append(int(input("enter a number 1:")))
numbers.append(int(input("enter a number 2:")))
numbers.append(int(input("enter a number 3:")))
numbers.append(int(input("enter a number 4:")))
numbers.append(int(input("enter a number 5:")))
numbers.append(int(input("enter a number 6:")))
counter = 0
if counter == len(numbers):
    print("good by")
else:
    press = input("press enter")
    if press:
        if numbers[counter] % 2 == 0:
            print(numbers[counter])
        counter += 1


if counter == len(numbers):
    print("good by")
else:
    press = input("press enter")
    if press:
        if numbers[counter] % 2 == 0:
            print(numbers[counter])
        counter += 1


if counter == len(numbers):
    print("good by")
else:
    press = input("press enter ")
    if press:
        if numbers[counter] % 2 == 0:
            print(numbers[counter])
        counter += 1



if counter == len(numbers):
    print("good by")
else:
    press = input("press enter ")
    if press:
        if numbers[counter] % 2 == 0:
            print(numbers[counter])
        counter += 1




