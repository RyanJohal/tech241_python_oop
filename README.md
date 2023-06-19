# Python OOP

### Classes and Instantiation
```python
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


```

### Abstraction
```python
# Abstraction
# Animal class

class Animal:

    def __init__(self):
       self.alive = True # Attributes
       self.spine = True # Attributes
       self.eyes = True # Attributes
       self.lungs = True # Attributes

    def breathe(self): # Methods
        print("One breath at a time, in and out")

    def eat(self): # Methods
        print("Nom Nom Nom")

    def procreate(self): # Methods
        print("Time to find a mate")

    def move(self): # Methods 
        print("Onwards and upwards")

# breathe is abstracted
cat = Animal()
cat.breathe()
```


### Inheritance  
```python
# Inheritance OOP

from python_oop.animal import Animal


class Reptile(Animal): # Inhertitance 

    def __init__(self): # Constructor
        super().__init__() # initialises the parent/base class - inherit everything from Animal
        self.cold_blooded = True # Attributes
        self.tetrapod = None # Attributes # Not all reptiles have 4 legs
        self.heart_chambers = [3, 4] # Attributes
        self.amniotic_eggs = None # Attributes # Not True for all reptiles

    def __seek_heat(self): # Methods
        return "it's chilly outside, I need a sunbed"

    def _show_seek_heat(self): # Methods
        print(self.__seek_heat())

    def hunt(self): # Methods
        print("Hunting prey")

    def use_venom(self): # Methods
        print("If I have it, may as well use it")

    def attract_mate_through_scent(self): # Methods
        print("Time to put on the aftershave")

bulbasaur = Reptile()
bulbasaur.hunt()
bulbasaur.breathe() # Animal method
```

### Using encapsulation from the previous class (_)
```python
# Showcasing encapsulation

from reptile import Reptile

class Snake(Reptile):

    def __init__(self):
        super().__init__()
        self.forked_tongue = True
        self.cold_blooded = True
        self.venom = None
        self.limbs = False
        self.tetrapod = False

    def use_tongue_to_smell(self):
        print("Do I say it smells nice, or tastes nice...?")

sidney = Snake()

sidney.breathe() # Animal method
sidney.use_tongue_to_smell() # Snake method

# Encapsulation is also really good, for protecting important variables/objects

# Types of modifiers in Python -

# Public - Anyone, Anywhere can use it
# Private - Accessible only within the class itself
# Protected - Accessible within the class and it's subclasses

#sidney.__seek_heatt() # Reptile method private
sidney._show_seek_heat()

```

```python
# Showcasing Polymorphism
# Methods can have the same name but act differently

from snake import Snake

class Python(Snake):

    def __init__(self):
        super().__init__()
        self.large = True
        self.two_lungs = True
        self.venom = False

    def digest_large_prey(self):
        print("ok, hand me the stretchy pants")

    def constrict(self):
        print("and...squeeeeeze")

    def climb(self):
        print("up we go")

    def shed_skin(self):
        print("I'm growing out of this now")

    def breathe(self):
        print("I am breathing but I am a Python!")
```

### OOP Classes
Attributes: Attributes are the data variables that hold information about the state of an object. They represent the characteristics or properties of the object. Attributes can be variables of various data types such as numbers, strings, lists, etc., and are defined within the class.

Methods: Methods are functions that are defined within a class and are responsible for performing actions or operations on objects. They can manipulate the object's attributes and provide behavior specific to the class. Methods are used to define the functionality of an object.

Objects: Objects are instances of a class. They are created from the class blueprint and represent individual entities with their own unique set of attributes and values. Objects are created using the class constructor and can be assigned to variables.
<img src="C:\Users\ryanj\Downloads\MicrosoftTeams-image (1).png"/>
<img src="C:\Users\ryanj\Downloads\MicrosoftTeams-image (2).png"/>



### OOP Four Pillars
Encapsulation: Encapsulation bundles data and methods within a class, hiding internal details and exposing a defined interface. It ensures data protection, code organization, and abstraction.

Inheritance: Inheritance allows a class to inherit attributes and methods from a parent class. The child class can reuse and extend the code of the parent class, promoting code reusability and creating specialised classes.![](C:\Users\ryanj\Downloads\MicrosoftTeams-image.png)

Polymorphism: Polymorphism enables objects of different classes to be treated as objects of a common superclass. It allows objects to take on different forms and respond differently to the same method. Polymorphism enhances code flexibility and modularity through method overriding and overloading.

Abstraction: Abstraction hides complex implementation details and provides a simplified interface. It focuses on defining essential features while suppressing irrelevant details. Abstract classes and interfaces enforce common behavior and promote maintainability and modular design.