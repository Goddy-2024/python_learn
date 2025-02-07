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
        self.__balance = balance #__balance is created as a private variable
    def deposit(self, amount):
        self.__balance += amount
    def get_balance(self):
        return self.__balance
acc = BankAcc(int(input("Enter Your account balance before deposit: ")))
acc.deposit(int(input("Enter the amount you wish to deposit: ")))
print("Your account balance after deposit: " + str(acc.get_balance()))
