#A program to has methods to boook a ticket, get status and get fare of a ticket from to to fro ..information of train running under a particular train number.
from random import randint
class Train:
    def __init__(self, train_number):
        self.train_number= train_number
    
    def book_ticket(self, from_station, to_station):
        print(f"Ticket booked from {from_station} to {to_station} on train {self.train_number}.")

    def get_status(self):
        print(f"Train {self.train_number} is running on time.")

    def get_fare(self, from_station, to_station):
        print(f"The fare from {from_station} to {to_station} on train {self.train_number} is {randint(1000, 5000)} rupees.")

# Example usage
train = Train("12345")
train.book_ticket("Ayodhya jn", "blr CANT")
train.get_status()
train.get_fare("Ayodhya jn", "blr CANT")