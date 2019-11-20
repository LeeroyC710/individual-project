class Animal():
    def __init__(self, type):
        self.type = type

class lion(Animal):
    def __init__(self, name):
        super().__init__("mammal")
        self.name  = name

pet = lion("Tinger")
print(pet.type)
