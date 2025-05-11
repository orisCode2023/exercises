class Person:
    def __init__(self, name='Shooki', age=20):
        self.__name = name
        self.__age = age

    def say(self):
        return "Hi :)"

    def __str__(self):
        return "Person {} is {} years old". \
            format(self.__name, self.__age)

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age


class Teacher(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def say(self):
        return "Good Morning"


class Student(Person):
    def __init__(self, name, age, grades, avg):
        super().__init__(name, age)
        self.grades = grades
        self._avg = avg

    def set_avg(sel, sum, counter):
        print(f"The average is {sum / counter} ")

    def get_avg(self):
        return self._avg



