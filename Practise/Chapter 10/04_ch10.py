# This code is part of a Python project demonstrating class methods and static methods.
class Calculator:
    def __init__(self, n):
        self.n = n 
    
    def square(self):
        print(f"The square is {self.n*self.n}")

    def cube(self):
        print(f"The cube is {self.n*self.n*self.n}")

    def squareroot(self):
        print(f"The squareroot is {self.n**0.5}")
    
    @staticmethod
    def hello():
        print("Hello human!")

x = Calculator(4)
x.hello()
x.square()
x.cube()
x.squareroot()