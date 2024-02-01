from bank_accounts import *

Dave = BankAccount(1000, 'Dave')
Sare = BankAccount(2000, 'Sare')


Dave.getBalance()
Sare.getBalance()

Sare.deposit(500)


Dave.deposit(500)


Dave.transfer(10, Sare)


Jim = InterestRewardsAcct(1000, "Jim")

Jim.getBalance()
Jim.deposit(100)
Jim.transfer(100, Dave)


Blaze = SavingsAccount(1000, "Blaze")

Blaze.getBalance()

Blaze.deposit(100)

Blaze.transfer(1000, Sare)