class CreditCard:
	""" A customer credit card """

	def __init__(self, customer, bank, account, limit):
		"""
		Create a new credit card instance.

		The initial balance is zero.

		customer --> The name of customer 
		bank --> the name of the bank 
		acnt --> the account identifier 
		limit --> credit limit 
		"""

		self._customer = customer
		self._bank = bank
		self._account = account
		self._limit = limit
		self._balance = 0

	def get_customer(self):
		""" Return name of the cutomer """
		return self._customer

	def get_bank(self):
		""" Return name of the bank """
		return self._bank

	def get_account(self):
		""" Return the card identifying number (typically stored in string) """
		return self._account

	def get_limit(self):
		""" Return current credit limit """
		return self._limit

	def get_balance(self):
		""" Return current balance """
		return self._balance

	def charge(self, price):
		""" Charge given price to the card, assuming sufficient credit limit 

		Return True if charge was processed; False if charge was denied.
		"""

		if price + self._balance > self._limit:
			return False 
		else:
			self._balance += price
			return True


	def make_payment(self, amount):
		""" Process customer payment that reduces balance """
		self._balance  -= amount
#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------
"""
INHERITENCE :

A hierarchial design is useful in software development, as common functionality can be grouped at the
most general level, thereby promoting reuse of code, while differentialted behaviours can be viewed as 
extensions of the general case, In ibject oriented programming, the mechanism for a modular and heirar-
chial organization is a technique known as inheritence.
This allows a new class to be defined based upon an existing class as the starting point. In object-
oriented terminlogy, the existing class is typically described as the base class, parent class, or 
super-class, while the newly defined class is known as the subclass or child class.

There are two ways in which a sublass can defferentiate itself from its superclass :
  * A subclass may specialize an exxisting behaviour by providing a new implementation that overides an
    existing method.
  * A subclass may also extend its superclass by providing brand new methods.

EXTENDING THE CreditCard CLASS :

The new class will differ from original in two ways :

  * if attempted charge is rejected because it would have exceeded the credit limit a $5 fee will be
    charged
  * there will be a mechanism for acessing a monthly interest charge on the outstanding balance, based 
    upon an Annual Percentage Rate (APR) specified as a constructor parameter.
"""
#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------
class PredatoryCreditClass(CreditCard):
	""" An extension to CreditCard that compounds interest and fees """

	def __init__(self, customer, bank, anct, limit, apr):
		""" Create a new predatory credit card instance 

		The initial balance is zero 

		customer --> the name of the customer 
		bank --> the name of the bank 
		acnt --> the account identifier 
		limit --> cedit limit 
		apr --> annual percentage rate 

		"""
		super().__init__(customer, bank, acnt, limit)  # call super constructor 
		self._apr = apr

	def charge(self, price):
		""" Charge given price to the card, assuming sufficient credit limit.

		Return True if charge was processed 
		Return False and asses $5 fee if charge is denied 
		"""
		success = super().charge(price)  # call inherited method 
		if not success:
			self._balance += 5 # assess penality 
		return success # caller expects return value 

	def process_month(self):
		""" Assess monthly interest on outstanding balance """
		if self._balance > 0:
			# if positive balance, convert APR to monthly multiplicative factor 
			monthly_factor = pow(1 + self._apr, 1/12)
			self._balance *= monthly_factor
#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------
if __name__ == '__main__':

	wallet = []

	wallet.append(CreditCard('Rahul Deshpande', 'State Bank Of India', '5391 0375 9387 5309', 2500))
	wallet.append(CreditCard('Nana Patekar', 'Saraswat Bank', '3485 0399 3395 1954', 3500))
	wallet.append(CreditCard('Yogendra Jogi', ' Bank Of India', '5391 0375 9387 5309', 5000))
	
	for val in range(1, 17):
		wallet[0].charge(val)
		wallet[1].charge(2*val)
		wallet[2].charge(3*val)

	for c in range(3):
		print('Customer : ', wallet[c].get_customer())
		print('Bank : ', wallet[c].get_bank())
		print('Account : ', wallet[c].get_account())
		print('Limit : ', wallet[c].get_limit())
		print('Balance : ', wallet[c].get_balance())
		

		while wallet[c].get_balance() > 100:
			wallet[c].make_payment(100)
			print('New balance = ', wallet[c].get_balance())
		print()
