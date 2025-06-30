# class MyMap:
#
#     def __init__(self, size = 8):
#         self.key = None
#         self.value = None
#         self.dic = [[self.key, self.value]]
#
#
#     def resize(self, lst):
#         new_size = (len(lst) + 1)
#         new_list = [None] * new_size
#         new_list = lst
#         lst = new_list
#         return lst
#
#     def append_list(self, lst, value):
#         if len(lst) == 0:
#             lst = self.resize(lst)
#             lst[0] = value
#         else:
#             lst = self.resize(lst)
#             lst[len(lst) - 1] = value
#         return lst
#
#     def is_empty(self, dic):
#         return len(dic) == 0
#
#     def update(self, key, value):
#         key_hash = self.get_hash_key(key)
#         self.dic[key_hash] = value
#         # if self.is_empty(self.dic):
#         #     self.dic = self.resize(self.dic)
#         # else:
#
#
#     def get_value(self, key):
#         for i in range(len(self.dic)):
#             if self.dic[i][0] == key:
#                 return self.dic[i][1]
#
#     def remove(self, key):
#         for i in range(len(self.dic)):
#             if self.dic[i][0] == key:
#                 self.dic[i][0] = self.dic[i][1] = None
#
#     def get_hash_key(self, key):
#         return key % len(self.dic)
#
#
#     def __str__(self):
#         return f"The key is {self.dic[self.key]} : the value is {self.dic[self.value]}"
#
#
# def main():
#     my_dic = MyMap()
#
#
# if __name__ == "__main__":
#     main()
my_list = [None, None, None, None, None, None, None, None, None, None]


def hash_function(value):
    sum_of_chars = 0
    for char in value:
        sum_of_chars += ord(char)

    return sum_of_chars % 10


print("'Bob' has hash code:", hash_function('Bob'))


def add(name):
    index = hash_function(name)
    my_list[index] = name


add('Bob')
add('Pete')
add('Jones')
add('Lisa')
add('Siri')
print(my_list)
