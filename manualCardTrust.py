#Sets genereal information about the balance, tax, cardholder, adn
# Trueted vendors. Generally, the information in these would be
# sent into our programe, not here here , we create it manually
# to test out our code
balance = 20.0
salesTax = 1.08
cardholderName = 'David Joyner'
trustedVender = ["Maria's", "bob s","Vrushali's", "Ling's", "Tia's"]

purchesePrice = 19.0
customerName = "David Joyner"
vender = "Vrushali's"
#This long conditional checks whetehr the balance is greate then
# the total price, whether the cardholder is also the customer,
# and the whether the vener is trusted
if balance>purchesePrice * salesTax and cardholderName ==\
		customerName and vener in trustedVender:
		print("Purchese Approved")
else:
	print("Purchese not Approved")
print("Done!")
