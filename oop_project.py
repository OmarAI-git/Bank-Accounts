from bank_accounts import *

omar = BankAccount(1000, 'Omar')
ali = BankAccount(500, 'Ali')

omar.deposit(1000)

ali.withdraw(1000)
ali.withdraw(300)

omar.transfer(10000, ali)
omar.transfer(200, ali)

ahmed = InterestRewardAcct(1000, 'Ahmed')

ahmed.get_balance()

ahmed.deposit(100)

ahmed.transfer(300, omar)

mohammed = SavingAcct(800, 'Mohammed')

mohammed.get_balance()

mohammed.deposit(100)

mohammed.transfer(1000, omar)
mohammed.transfer(200, omar)