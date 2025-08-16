#calculator to calculate square, cube, and square root of a number

class Calculator:
    def __init__(self, number):
        # Store the input number when creating the object
        self.number = number

    def square(self):
        """Return the square of the number."""
        return self.number ** 2

    def cube(self):
        """Return the cube of the number."""
        return self.number ** 3

    def square_root(self):
        """Return the square root of the number."""
        return self.number ** 0.5


# Example usage
x = Calculator(4)
print(x.square())       # 16
print(x.cube())         # 64
print(x.square_root())  # 2.0
