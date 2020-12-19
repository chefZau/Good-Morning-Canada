menu = {
	"egg" : 0.99,
	"bacon" : 0.49,
	"sausage" : 1.49,
	"hash brown" : 1.19,
	"toast" : 0.79,
	"coffee" : 1.49,
	"tea" : 1.09
}

def formatInput(textLine):
	"""
	the purpose of this funciton is to clean
	leading and trailing spaces, including 
	cases when multiple spaces separate words
	
	:param: textLine: the input text
	"""
	textLine = textLine.lower().strip()
	wordList = textLine.split()
	textLine = " ".join(wordList)
	
	return textLine

def isValidItem(userInput):
	"""
	the purpose of this function is to test 
	user input is valid or not
	
	:param userInput: user inputs
	"""
	return (userInput in menu.keys() or userInput in ["small breakfast", "regular breakfast", "big breakfast"])

before_tax = 0

while True:
	
	item = formatInput(input("Enter item (q to terminate): small breakfast, regular breakfast, big breakfast, egg, bacon, sausage, hash brown, toast, coffee, tea:")) 
	
	if item == "q": break

	while not isValidItem(item):
		item = formatInput(input("*** Invalid Item, Please Re-enter: ")) 
	
	combo = 0
	if item == "small breakfast":
		combo += menu["egg"] + menu['hash brown'] + 2 * menu['toast'] + 2 * menu['bacon'] + menu['sausage']
	elif item == "regular breakfast":
		combo += 2 * menu["egg"] + menu['hash brown'] + 2 * menu['toast'] + 4 * menu['bacon'] + 2 * menu['sausage']
	elif item == "big breakfast":
		combo += 3 * menu["egg"] + 2 * menu['hash brown'] + 4 * menu['toast'] + 6 * menu['bacon'] + 3 * menu['sausage']

	quantity = input("Enter quantity:")
	while not quantity.isnumeric():
		quantity = input("*** Invalid Quantity, Please Re-enter: ")

	before_tax += float(quantity) * menu[item] if combo == 0 else combo * float(quantity)

tax = round(before_tax * 0.13, 2)
total = round(before_tax + tax, 2)

print("\nCost  : {:>8.2f}\nTax   : {:>8.2f} \nTotal : {:>8.2f}\n".format(before_tax, tax, total))