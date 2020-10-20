#!/usr/bin/python3

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

def format_output(eta, loops, w0, w1, error):
	out = "CS-5001: HW#1 \nProgrammer: Mitchell Meier\n\nTRAINING: \nUsing learning rate eta = " + str(eta) + "\nUsing " + str(loops) + " iterations. \n\nOUTPUT: \nw0 = " + str(w0) + "\nw1 = " + str(w1) + "\n\nVALIDATION \nSum-of-Squares Error = " + str(error)
	print(out)


def y_hat(weight0, weight1, inp):
	return weight0 + (weight1 * inp)

def learn(eta, loops, t, v):
	w0 = secrets.randbelow(50) + 1
	w1 = secrets.randbelow(50) + 1

	for i in range(loops):
		for k in t:
			cap = y_hat(w0, w1, k.cookies)
			delta = k.chips - cap
			w0 = w0 + eta * delta
			w1 = w1 + eta * delta * k.chips

	err = 0
	for i in v:
		err += (i.chips - y_hat(w0, w1, i.cookies)) ** 2

	format_output(eta, loops, w0, w1, err)


#Main
training = parse_input('chocodata.txt')
validation = parse_input('chocovalid.txt')

#Chosen eta as 1*10^-6, and iterations at 1*10^5
learn(0.000001, 100000, training, validation)