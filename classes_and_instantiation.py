# Classes

# creating a class - this is a template
class Dog:
    animal_kind = "canine" # class variable

    def bark(self): # class function = methods
        self.animal_kind
        return "woof"
# print(Dog.animal_kind)
# print(Dog.bark(Dog))

# Instantiation of a class

fido = Dog()
lassie = Dog()

print(type(fido)) # <class '__main__.Dog'>
print(fido.animal_kind) # canine
print(lassie.animal_kind)
print(fido.bark()) # woof
print(lassie.bark())

# Class variables can be overwritten
fido.animal_kind = "Big Dog"
print(fido.animal_kind) # canine
print(lassie.animal_kind)

# Be careful of class variables

# Dog.animal_kind = "Dolphin"
# print(lassie.animal_kind)
# print(lassie.bark())
