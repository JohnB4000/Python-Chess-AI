import copy

class Person():
    def __init__(self, value2: int):
        self.value2 = value2

    def display(self):
        print(self.value2)


obj1 = [Person(1), Person(2)]
obj2 = copy.deepcopy(obj1)
obj2[1] = Person(3)

print(obj1)
print(obj2)