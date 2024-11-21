#Classes and Objects
#Q1
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p1=Person("Spriha",18)
p2=Person("ABCD",19)
print("Name : ",p1.name)
print("Age :",p1.age)
print("Name : ",p2.name)
print("Age :",p2.age)
#Q2
class Student:
    def __init__(self,name="John",age=19):
        self.name=name
        self.age=age
    def getinfo(self):
        print("Name : ",self.name)
        print("Age : ",self.age)
s1=Student()
s2=Student("Spriha",18)
s3=Student("ABCD",23)
s1.getinfo()
s2.getinfo()
s3.getinfo()
#Q3
class account:
    def __init__(self,bal):
        self.bal=bal
    def credit(self):
        bal=self.bal
        amount=int(input("Enter amount to be credited into account : "))
        self.bal=bal+amount
        print("Amount credited successfully.")
        self.checkbalance()
    def debit(self):
        bal=self.bal
        amount=int(input("Enter amount to be debited from account : "))
        self.bal=bal-amount
        print("Amount debited successfully.")
        self.checkbalance()
    def checkbalance(self):
        print("Current balance : ",self.bal)
a1=account(10000)
a1.checkbalance()
a1.credit()
a1.debit()
