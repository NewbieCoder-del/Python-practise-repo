class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin
    def __str__(self):
        return f"{self.name} works at {self.company} with a salary of {self.salary} and pin {self.pin}"

pr1 = Programmer("Harish", 124500, 40001)
print(pr1) # This will use the __str__ method to print the object details
#print(pr1.name, pr1.salary, pr1.pin, pr1.company)
pr2 = Programmer("Roshni", 120087, 45001)
print(pr2) # This will use the __str__ method to print the object details
#print(pr2.name, pr2.salary, pr2.pin, pr2.company)