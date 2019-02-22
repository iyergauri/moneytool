import pandas as pd

lst = {
	"Gauri" 	: 14.33,
	"Megan" 	: 17.88,
	"Katrina" 	: 16.99,
	"Izze"		: 15.82
}

total = 80.00

########################################################################
subtotal = 0
total *= 100
for name, cost in lst.items():
	lst[name] = cost * 100
	subtotal += (cost * 100)

taxAndTip = total - subtotal

if taxAndTip < 0:
	raise ValueError("Subtotal was greater than total!")

for name, cost in lst.items():
	contrib = int((cost/subtotal) * taxAndTip)
	lst[name] += contrib
	print("{} pays ${:.2f} (${:.2f} original + {:.2f}% of the tax, which is ${:.2f})".format(
		name,
		lst[name] / 100,
		cost / 100,
		(cost/subtotal),
		contrib/100
	))
	lst[name] /= 100

# print(lst)
