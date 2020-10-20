import secrets

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
		ret.append(Data(int(cks), int(chs)))
	return ret

def y_hat(weight0, weight1, inp):
	return weight0 + (weight1 * inp)


training = parse_input('chocodata.txt')
validation = parse_input('chocovalid.txt')


#Main
eta = 0.00001

w0 = secrets.randbelow(50) + 1
w1 = secrets.randbelow(50) + 1


for i in range(1000):
	for k in training:
		cap = y_hat(w0, w1, k.cookies)
		delta = k.chips - cap
		w0 = w0 + eta * delta * k.chips
		w1 = w1 + eta * delta * k.chips

print(w0)
print(w1)

current = 0
for i in validation:
	current += (i.chips - y_hat(w0, w1, i.cookies)) ** 2

print(current)