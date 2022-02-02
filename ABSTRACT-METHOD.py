from abc import ABC, abstractmethod


class bank(ABC):
    @abstractmethod
    def loan(self): pass

    @abstractmethod
    def credit(self): pass

    @abstractmethod
    def debit(self): pass

class HDFC(bank):
    def loan(self):
        print("we can provide 7.5% intrest loan")
    def credit(self):
        print("we can provide credit")

    def debit(self):
        print("we can provide debit")

    def card(self):
        print("we can provide credit card")

o=HDFC()
o.loan()
o.card()
o.debit()
o.card()
#CODE WITH ❤ BY SABARIRAJKUMAR️