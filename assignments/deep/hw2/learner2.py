#!/usr/bin/python3

import random
import math

class Data:

	def __init__(self, sz, cl, ty):
		self.size = sz
		self.color = cl
		self.type = ty

	def debug_print(self):
		print("Size: " + str(self.size), end=', ')
		print("Color: " + str(self.color), end=', ')
		print("Type: " + str(self.type))



def parse_input(inp):
	reader = open(inp, 'r')
	temp = reader.readlines()
	reader.close()
	ret = []
	for i in temp:
		size = i.split('\t')[0]
		color = i.split('\t')[1]
		ty = i.split('\t')[2].replace('\n', '')
		ret.append(Data(int(size), int(color), int(ty)))

	return ret

def format_output(eta, loops, w0, w1, w2, error):
	out = str(w0) + " " + str(w1) + " " + str(w2) + "\n\n"
	out += "CS-5001: HW#2 \nProgrammer: Mitchell Meier\n\nTRAINING: \nUsing learning rate eta = " + str(eta) + "\nUsing " + str(loops) + " iterations. \n\nOUTPUT: \nw0 = " + str(w0) + "\nw1 = " + str(w1) + "\nw2 = " + str(w2) + "\n\nVALIDATION \nSum-of-Squares Error = " + str(error)
	print(out)
	writer = open("learner2output.txt", "w")
	writer.write(out)
	writer.close()


def sigmoid(x):
	if x >= 0:
		z = math.exp(-x)
		return 1 / (1 + z)
	else:
		z = math.exp(x)
		return z / (1 + z)


def y_hat(weight0, weight1, weight2, x1, x2, is_training):
	margin = 0.0001
	cap = weight0 + (weight1 * x1) + (weight2 * x2)
	flattened = sigmoid(cap)
	if is_training:
		return max(min(flattened, 1-margin), margin)
	else:
		return flattened

def rand_num():
	return random.uniform(-2, 2)

def learn(eta, loops, t, v):
	w0 = rand_num()
	w1 = rand_num()
	w2 = rand_num()

	for i in range(loops):
		for example in t:
			cap = y_hat(w0, w1, w2, example.size, example.color, True)
			delta = example.type - cap
			update = eta * delta * cap * (1-cap)
			w0 = w0 + update
			w1 = w1 + update * example.size
			w2 = w2 + update * example.color
	

	err = 0
	for example in v:
		err += (example.type - y_hat(w0, w1, w2, example.size, example.color, False)) ** 2

	format_output(eta, loops, w0, w1, w2, err)


#Main
training = parse_input('appledata.txt')
validation = parse_input('applevalid.txt')

learn(0.01, 100000, training, validation)
