from abc import ABC, abstractmethod

class Bank(ABC):
    def __init__(self, amount):
        self.amount = amount
    
    @abstractmethod
    def get_balance(self):
        pass
    
    @abstractmethod
    def deposit(self, amount):
        """Subclasses must implement their own deposit logic"""
        pass
    
    @abstractmethod
    def withdraw(self, amount):
        """Subclasses must implement their own withdrawal logic"""
        pass

class Sbi_atm(Bank):
    MIN_BALANCE = 500
    
    def __init__(self, balance):
        super().__init__(balance)  # ✅ Call parent constructor
    
    def get_balance(self):
        return self.amount
    
    def deposit(self, amount):
        if amount > 0:
            self.amount += amount
            print(f"[SBI] Deposited {amount}. Balance: {self.amount}")
        else:
            print("Invalid deposit amount")
    
    def withdraw(self, amount):
        if amount > 0 and self.amount - amount >= self.MIN_BALANCE:
            self.amount -= amount
            print(f"[SBI] Withdrawn {amount}. Balance: {self.amount}")
        else:
            print(f"Cannot withdraw. Minimum balance: {self.MIN_BALANCE}")

class Icici_atm(Bank):
    MIN_BALANCE = 1000
    
    def __init__(self, balance):
        super().__init__(balance)
    
    def get_balance(self):
        return self.amount
    
    def deposit(self, amount):
        if amount > 0:
            self.amount += amount
            print(f"[ICICI] Deposited {amount}. Balance: {self.amount}")
        else:
            print("Invalid deposit amount")
    
    def withdraw(self, amount):
        if amount > 0 and self.amount - amount >= self.MIN_BALANCE:
            self.amount -= amount
            print(f"[ICICI] Withdrawn {amount}. Balance: {self.amount}")
        else:
            print(f"Cannot withdraw. Minimum balance: {self.MIN_BALANCE}")

ob1 = Sbi_atm(1000)
print(f"SBI Balance: {ob1.get_balance()}")
ob1.deposit(500)
ob1.withdraw(200)
ob1.withdraw(1000)  # ❌ Fails (violates min balance)

print("\n" + "="*40 + "\n")

ob2 = Icici_atm(2000)
print(f"ICICI Balance: {ob2.get_balance()}")
ob2.deposit(1000)
ob2.withdraw(500)
ob2.withdraw(1500)  # ❌ Fails (violates min balance)