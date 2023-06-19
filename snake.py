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