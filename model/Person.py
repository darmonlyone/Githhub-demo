class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def change_name(self, name):
        self.name = name

    def change_age(self, age):
        pass

    def __repr__(self):
        """
        :return: 'name age years old'
        """
        return f"{self.name} {self.age} years old"
