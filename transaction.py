class Transaction:
	def __init__(self, payer, title, payees, total):
		self.payer = payer
		self.title = title
		self.payees = payees
		self.total = total

	def print(self):
		print("\n==============================")
		print("{} paid for {}: ".format(self.payer, self.title))
		for name, amt in self.payees.items():
			if (name == self.payer):
				print("\tthemselves:\t{}".format(amt))
			elif (len(name) < 7):
				print("\t{}:\t\t{}".format(name, amt))
			else:
				print("\t{}:\t{}".format(name, amt))
		print("==============================\n")

x = Transaction("Gauri", "drinks",
	{"Gauri" : 14, "Megan" : 16, "Izze" : 20, "Katrina" : 13},
	35)
y = Transaction("Izze", "food",
	{"Gauri" : 12, "Megan" : 11, "Izze" : 9, "Katrina" : 8},
	35)

transactions = [x, y]
for t in transactions:
	t.print()
