class Person:  # Class attributes, attributes specific to class not to instance(object)
    number_of_people = 0

    def __init__(self, name):
        self.name = name
        Person.add_person()

    # decorator, denote that methode is class methode, act on the class, not instance
    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1


print(Person.number_of_people)
p1 = Person("tim")
p2 = Person("jill")
print(Person.number_of_people_())
