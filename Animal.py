class Animal:
    def make_sound(self):
        pass
class Cat(Animal):
    def make_sound(self):
        print("meow")
class Dog(Animal):
    def make_sound(self):
        print("Bow")
for v in [Cat(), Dog()]:
    v.make_sound()