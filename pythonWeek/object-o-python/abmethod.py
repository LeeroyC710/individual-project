from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, type):
        self.type = type


    def speak(self):
        pass

class lion(Animal):
    def __init__(self, name):
        super().__init__("Mammal")
        self.name  = name

    def speak(self):
        return "Roar"
    
cab = lion("cat")
print(cab.type)
print(cab.speak())
