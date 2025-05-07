class Animal:
    def __init__(self , animal= None):
        self._name  = "dog"
        self._age = 3

    def _set_name_(self , name = ""):
        self._name = name

    def update_birthday(self):
        self._age += 1

    def get_age(self):
        return self._age

    def get_name(self):
        return self._name

    def __str__(self):
        return f"The animal name is: {self.get_name()} and it is {self.get_age()} years old"

def main():
    animal1 = Animal()
    animal1.update_birthday()
    animal1._set_name_("beni")
    print(animal1)


if __name__ == "__main__":
    main()
