import re

class Data:
	def __init__(self, ck, ch):
		self.cookies = ck
		self.chips = ch

	def debug_print(self):
		print("Cookies: " + str(self.cookies), end=', ')
		print("Chips: " + str(self.chips))


def parse_input(inp):
	reader = open(inp, 'r')
	temp = reader.readlines()
	reader.close()
	ret = []
	for i in temp:
		cks = i.split('\t')[0]
		chs = i.split('\t')[1].replace('\n', '')
		ret.append(Data(cks, chs))
	return ret


training = parse_input('chocodata.txt')
validation = parse_input('chocovalid.txt')


