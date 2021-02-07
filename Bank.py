class Bank():
    def __init__(self,total,fdAmount ,cardNumber,pin):
        self.total = int(total)
        self.fdAmount = int(fdAmount)
        self.cn = int(cardNumber)
        self.pin = int(pin)
        print(self.total)
    def debit(self):
        total = str(self.total)
        fdAmount = str(self.fdAmount)
        cn  = str(self.cn)
        pin = str(self.pin)
        fdTotalAmt = self.fdAmount + (5/100*self.fdAmount)
        print("Your Fixed Deposit of ruppes " , fdAmount , " will mature in 1 year 1 day and will amount to " , fdTotalAmt )

Citi = Bank("500000","2000","1278956847","1877")
Citi.debit()
