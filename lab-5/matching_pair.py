#sub
#greedy
import re


def pair(txt):
	"""
	this funciton finds any repeated word
	"""
	for m in re.finditer(r'\b(\w+?)\s?\1+', txt, re.I):
		print(f'{m.start()}-{m.end()}: {m.group(1)}')


def autoCorrect(repeated):
	return repeated.group(1)


if __name__ == "__main__":
	txt = "the thethethe quick brown fox jumps overoveroverover the lazy dog"
	pattern = re.compile(r'\b(\w+?)\s?\1+', re.I)
	x = pattern.subn(string=txt, repl=autoCorrect)
	print(x)
	pair(txt)
