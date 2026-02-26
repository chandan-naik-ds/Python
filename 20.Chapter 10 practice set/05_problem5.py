from random import randint

class Train:
    
    def __init__(self,trainNo):
        self.trainNo = trainNo
    
    def book(self,fro,to):
        print(f"Ticket is booked in train No.: {self.trainNo} from {fro} to {to}")

    def getStatus(self):
        print(f"The train of number {self.trainNo} is running on time")

    def getFare(self, fro, to):
        print(f"Ticket is fare in train No. : {self.trainNo} from {fro} to {to} is {randint(100,500)} ")

t = Train(19339)
t.book("Murudeshwar","Kundapura")
t.getStatus()
t.getFare("Murudeshwar","Kundapura")
