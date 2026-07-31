''' Q:Payment System (Runtime Polymorphism)
An online store supports multiple payment methods: CreditCard, UPI, and
NetBanking. Create a base class Payment with a method process_payment() and
override it in each payment type.'''

class Payment:
    def process_payment(self):
        print("Processing Payment...")

class CreditCard(Payment):
    def process_payment(self):
        print("Payment done using Credit Card")

class UPI(Payment):
    def process_payment(self):
        print("Payment done using UPI")

class NetBanking(Payment):
    def process_payment(self):
        print("Payment done using Net Banking")

p1 = CreditCard()
p2 = UPI()
p3 = NetBanking()
payments = [p1, p2, p3]
for payment in payments:
    payment.process_payment()