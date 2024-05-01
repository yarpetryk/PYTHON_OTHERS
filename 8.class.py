class Person:
    _age = 36

    def __init__(self, name):
        self.name = name
        print('My name is %s' % self.name)

    # def party(self, bottle):
    #     self.bottle += bottle
    #     print('I take %d' % self.bottle, 'bottles')

class PersonOther(Person):
    pass

yar = Person('yaroslav')
roman = PersonOther('roman')
print(yar._age)
print(PersonOther._age)



# # ------------------------------------------------------------------------------------------------------
# class Student(Person):
#     def __init__(self, fullname, age):
#         super().__init__(fullname, age)
#
#     # def party(self,bottle):
#     #      super().party(bottle)
#
#     def party(self, bottle):  # overriding method party()
#         self.bottle += bottle * 5
#         print('I take %d' % self.bottle, 'bottles')
#
#     __secret = 10
#
#     def my_secret(self):
#         print(self.__secret + 100)
#
#
# john = Student('John', 29)
#
# for i in range(1, 5):
#     john.party(i)
#
# john.year = 2000
# print(john.year)
#
# john.my_secret()
#
# john._Student__secret  # access to invisible attr
# # print(john.__secret) #invisible outside
# # ------------------------------------------------------------------------------------------------------
# print(hasattr(john, 'year'))  # Returns true if 'age' attribute exists
# print(getattr(john, 'year'))  # Returns value of 'age' attribute
# setattr(john, 'year', 2020)  # Set attribute 'age' at 2020
# print(getattr(john, 'year'))  # Returns new value of 'age' attribute
# # delattr(john, 'year')    # Delete attribute 'age'
# # --------------------------------------------------------------------------------------------------------
# print(john.__dict__)  # Dictionary containing the class's namespace
# print(john.__doc__)  # Class documentation string or none, if undefined
# print(Person.__name__)  # Class name
# print(Person.__call__)  # Class name
#
# print(john.__module__)  # Module name in which the class is defined. This attribute is "__main__" in interactive mode.
# print(
#     Person.__bases__)  # A possibly empty tuple containing the base classes, in the order of their occurrence in the base class list.
# # ---------------------------------------------------------------------------------------------------------
# print(isinstance(john,
#                  Person))  # boolean function returns true if obj is an instance of class Class or is an instance of a subclass of Class
# print(issubclass(Student,
#                  Person))  # boolean function returns true if the given subclass sub is indeed a subclass of the superclass sup
# # ---------------------------------------------------------------------------------------------------------
# # __del__(self) delete the object
