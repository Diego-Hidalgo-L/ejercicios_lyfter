class BankAccount():
	balance = 0

	def __substract_balance(self, amount):
		self.balance -= amount

	def __add_balance(self, amount):
		self.balance += amount
		print(self.balance)

	def send_money_to_account(self, account, amount):
		self.__substract_balance(amount)
		account.__add_balance(amount)


bank_account = BankAccount()
bank_account.__add_balance(5000)