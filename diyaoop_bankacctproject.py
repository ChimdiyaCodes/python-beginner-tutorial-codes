from bank_accounts import *

Chimdiya = BankAccount(3000, "Chimdiya")
Nnaemeka = BankAccount(5000, "Nnaemeka")

Chimdiya.getBalance()
Nnaemeka.getBalance()

Nnaemeka.deposit(700)

Chimdiya.withdraw(10000)
Chimdiya.withdraw(500)

Chimdiya.transfer(10000, Nnaemeka)
Chimdiya.transfer(100, Nnaemeka)

Constance = InterestRewardsAcct(2000, "Constance")

Constance.getBalance()

Constance.deposit(300)

Constance.transfer(200, Nnaemeka)

Ada = SavingsAcct(1000, "Ada")

Ada.deposit(100)

Ada.transfer(200, Constance)
