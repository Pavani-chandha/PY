class Account:
    def setBalance(self,balance):
        self.__balance+=balance
acc=Account(name="abc",age=10)
print(acc.getBalance())
acc.setBalance(100)
print(acc.getBalance())
print(acc.__balance)