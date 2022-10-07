class Animal:
    animaltype="mammel"

    
class Pet(Animal):
    PetColor="White"

    
class Dog(Pet):
    Name="Labrador"

    @staticmethod
    def bark():
        print("Bow Bow")
    
d=Dog()
print(d.Name)
print(d.animaltype)
print(d.PetColor)
d.bark()
        