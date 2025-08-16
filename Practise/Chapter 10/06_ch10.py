from random import randint

class Train:

    def __init__(slf, trainNo):
        slf.trainNo = trainNo

    def book(hari, train_fro, train_to):
        print(f"Ticket is booked in train no: {hari.trainNo} from {train_fro} to {train_to}") 

    def getStatus(self):
        print(f"Train no: {self.trainNo} is running on time") 

    def getFare(self, train_fro, train_to):
        print(f"Ticket fare in train no: {self.trainNo} from {train_fro} to {train_to} is {randint(222, 5555)}")  


t = Train(12399)
t.book("Raipur", "Delhi")
t.getStatus()
t.getFare("Raipur", "Delhi")


