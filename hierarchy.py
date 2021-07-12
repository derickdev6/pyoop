class Person:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if new_name != self.__name and len(new_name.replace(' ', '')) > 0:
            self.__name = new_name
        else:
            print('Name must be different, no whitespaces only')

    @name.deleter
    def name(self):
        print(f'Deleting name {self.__name}')
        del self.__name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        if new_age != self.__age and new_age > 0:
            self.__age = new_age
        else:
            print('Age must be different, no negative')

    @age.deleter
    def age(self):
        print(f'Deleting age {self.__age}')
        del self.__age

    def salute(self, other):
        print(f'Hey {other.name}, my name is {self.__name}!')


class Student(Person):

    def __init__(self, name, age, career):
        super().__init__(name, age)
        self.__career = career

    @property
    def career(self):
        return self.__career

    @career.setter
    def career(self, new_career):
        if new_career != self.__career and len(new_career.replace(' ', '')) > 0:
            self.__career = new_career
        else:
            print('career must be different, no whitespaces only')

    @career.deleter
    def career(self):
        print(f'Deleting career {self.__career}')
        del self.__career

    # IMPORTANT, use name throught the getter,
    # and not directly since it doesn't belong to the Student class
    def sayCareer(self):
        print(f'''I'm {self.name}, and I study {self.__career}  ''')

    def salute(self, other):
        print(f'Hey {other.name}, my name is {self.name} and I am a student!')


derick = Student('Derick', 19, 'IT')
patrick = Person('Patrick', 23)

derick.salute(patrick)
patrick.salute(derick)
