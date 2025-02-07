#OOP Class and Object
class StudName:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    def describe(self):
        return f"My name is {self.fname} {self.lname}"
my_name = StudName("Godswill", "Omondi") 
print(my_name.describe())

#OOP in encapsulation of data
class BankAcc:
    def __init__(self, balance):
        self.__balance = balance
    def deposit(self, amount):
        self.__balance += amount
    def get_balance(self):
        return self.__balance
acc = BankAcc(26000)
acc.deposit(2000)
print(acc.get_balance())
