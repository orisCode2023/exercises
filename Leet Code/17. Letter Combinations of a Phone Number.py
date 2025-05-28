def casting_to_integer(num):
    return int(num)

def cast_to_str(num1, num2):
    return str(num1), str(num2)

def divide(num):
    last_num = num % 10
    num //= 10
    return num, last_num


def answer():
    arr = []
    dic = {}
    digits = input("enter numer ")
    dic.update({"2": "abc"})
    dic.update({"3": "def"})
    dic.update({"4": "ghi"})
    dic.update({"5": "jkl"})
    dic.update({"6": "mno"})
    dic.update({"7": "pqrs"})
    dic.update({"8": "tuv"})
    dic.update({"9": "wxyz"})

    if digits == "":
        return arr
    if len(digits) == 1:
        temp = dic[digits]
        arr = list(temp)
        return arr
    else:
        new_num = casting_to_integer(digits)
        idx1, idx2 = divide(new_num)
        idx1, idx2 = cast_to_str(idx1, idx2)
        for letter_idx1 in dic[idx1]:
            for letter_idx2 in dic[idx2]:
                arr.append(letter_idx1 + letter_idx2)





    return arr

print(answer())

