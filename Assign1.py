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