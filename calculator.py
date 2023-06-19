# Calculator

class Calculator:
    def __init__(self):
        self.sum = 0

    def addition(self, num, num2):
        self.sum = num + num2

    def subtract(self, num, num2):
        self.sum = num - num2

    def multiply(self, num, num2):
        self.sum = num * num2

    def divide(self, num, num2):
        self.sum = num / num2

calc = Calculator()
calc.addition(5, 5)
print(calc.sum)
calc.subtract(25, 6)
print(calc.sum)
calc.multiply(25, 6)
print(calc.sum)
calc.divide(90, 9)
print(calc.sum)