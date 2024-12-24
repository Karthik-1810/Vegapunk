"""class car:
    brake='STOP'
    def __init__(self,colour,model,name):
        self.colour=colour
        self.model=model
        self.name= name
        print(id(self))
    def start(self):
        print(f'start the car {self.name}')
    @classmethod
    def stop(cls):
        print(cls.brake)
        print()
swift=car('red','newmodel','karthi')
2762169001088
print(id(swift))
swift.start()
swift.stop()

class Animal:
    def sleep(self):
        print("The animal is sleeping")

    def make_sound(self):
        # Enforce that subclasses must implement this method
        raise NotImplementedError("Subclasses must implement this method")

class Dog(Animal):
    def bark(self):
        print("Bark")

class Cat(Animal):
    def bark(self):
        print("Bark")

dog = Dog()
dog.sleep()       # Output: The animal is sleeping
dog.bark()  # Output: Bark

cat = Cat()
cat.bark()  # Output: Meow

class Animal:
    def sleep(self):
        print("The animal is sleeping")

class Dog(Animal):
    def bark(self):
        print("Bark")

dog = Dog()
dog.sleep()
dog.bark()
class Payment:
    def process_payment(self, amount):
        raise NotImplementedError("Subclasses must implement this method")

class CreditCardPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing credit card payment of ${amount}")

class PayPalPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of ${amount}")"""

from abc import ABC, abstractmethod


# Abstract Base Class
class Payment(ABC):

    @abstractmethod
    def process_payment(self, amount):
        """Method that must be implemented by all subclasses."""
        print(f"Processing credit card payment of ${amount}")
        print('Hi')
        print('Bye')



# Subclass 1: Credit Card Payment
class CreditCardPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing credit card payment of ${amount}")


# Subclass 2: PayPal Payment
class PayPalPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of ${amount}")


# Subclass 3: Bank Transfer Payment (this class must also implement the method)
class BankTransferPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing bank transfer of ${amount}")


# Function to process any type of payment
def make_payment(payment_method: Payment, amount: float):
    payment_method.process_payment(amount)


# Real-time scenario
credit_card = CreditCardPayment()
paypal = PayPalPayment()
bank_transfer = BankTransferPayment()


make_payment(credit_card, 50)  # Output: Processing credit card payment of $50
make_payment(paypal, 75)  # Output: Processing PayPal payment of $75
make_payment(bank_transfer, 100)


