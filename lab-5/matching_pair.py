import re


def pair(txt):
	for m in re.finditer(r'\b(\w+)\s?\1', txt, re.I):
		print(f'{m.start()}-{m.end()}: {m.group()}')


if __name__ == '__main__':
	text = 'He he was carefully disguised butbut captured quickly by by police.'
	pair(text)
