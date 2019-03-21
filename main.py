import pandas as pd

lst = {
	"Emily" 	: 13.0,
	"Karen" 	: 13.0,
	"Gauri" 	: (21.0/7)+12+5,
	"Chris" 	: (21.0/7)+13,
	"Sfen" 		: (21.0/7)+13+4,
	"Allison" 	: (21.0/7)+13+4,
	"Vivian" 	: (21.0/7)+15,
	"Sam" 		: (21.0/7)+15,
	"Gus"		: (21.0/7)+13+5
}

total = 197
subtotal = 0
########################################################################
print("\n--- LISTED PRICE ---")
for k, v in lst.items():
	t = "\t\t" if len(k) < 7 else "\t"
	print("{}:{}${:.2f}".format(k, t, v))

total *= 100
for name, cost in lst.items():
	lst[name] = cost * 100
	subtotal += (cost * 100)

print("\nsubtotal = {}".format(subtotal/100))
taxAndTip = total - subtotal
print("\ntax and tip = {}".format(taxAndTip/100))

if taxAndTip < 0:
	raise ValueError("Subtotal was greater than total!")

for name, cost in lst.items():
	contrib = int((cost/subtotal) * taxAndTip)
	lst[name] += contrib

	lst[name] /= 100

# df = pd.read_json('log.json', lines=True)
# print(df)
print("\n--- PROPORTIONAL TAX/TIP ---")
for k, v in lst.items():
	t = "\t\t" if len(k) < 7 else "\t"
	print("{}:{}${:.2f}".format(k, t, v))

print()
