#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------

"""
Exmple : CreditCard Class 
provides a simple mdel for traditional credit cards. They have identifying information about 
the customer, bank, account number, credit limit, and current balance. The class restricts
charges that would cause a card's balance to gp over speed limit, but it does not change interests
or late payments.

The Self identifier :
In Python, the self identifier playes key role. Each instance stores its own instance variables, to 
reflect its current state.
Self, identifies the instance upon which a method is invoked.

"""
#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------
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
"""
The Constructor : 
This results in a call to the specifically named __init__ method that serves as a constructor of 
the class. Responsibility is to establish the state of a newly created credit card object with 
appropriate instance variables.

cc = CreditCard('John Doe', '1st Rank', '5391 0375 9387 5309', 1000)

Encapsulation :
Single leadning underscore in the name of a data member, such as _balance implies that it is inteded
as non public. Users pf a class should not directly access such members. This allows us to better 
enforce a consistent state for all instances. 

Testing the Class :
Tests are enclosed within conditional, if __name__ == '__main__', so that they can be embeded in the 
source code with the class defination. 

"""
"""

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
"""

#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------
# Output :
"""
Customer :  Rahul Deshpande
Bank :  State Bank Of India
Account :  5391 0375 9387 5309
Limit :  2500
Balance :  136
New balance =  36

Customer :  Nana Patekar
Bank :  Saraswat Bank
Account :  3485 0399 3395 1954
Limit :  3500
Balance :  272
New balance =  172
New balance =  72

Customer :  Yogendra Jogi
Bank :   Bank Of India
Account :  5391 0375 9387 5309
Limit :  5000
Balance :  408
New balance =  308
New balance =  208
New balance =  108
New balance =  8
"""
#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------