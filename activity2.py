from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCard(PaymentMethod):
    def pay(self, amount):
        print("Charging ", amount, "to credit card")

class Paypal(PaymentMethod):
    def pay(self, amount):
        print("Sending", amount, "via Paypal")

class Gcash(PaymentMethod):
    def pay(self, amount):
        print("Sending", amount, "via Gcash")

methods = [CreditCard(), Paypal(), Gcash() ]
for m in methods:
    m.pay(49.99) 