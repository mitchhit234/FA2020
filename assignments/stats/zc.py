#!/usr/bin/python3

from scipy.integrate import quad
import numpy as np

x = input("Enter variable value: ")
median = input("Enter mean value: ")
dev = input("Enter standard deviation: ")
sample = input("Enter a sample size: ")

if sample == 'n':
	z = (float(x) - float(median))/float(dev)
else:
	z = (float(x) - float(median))/(float(dev)/np.sqrt(float(sample)))
z = round(z,2)
print("Z = " + str(z) )

def normalProbabilityDensity(x):
	constant = 1 / np.sqrt(2 * np.pi)
	return(constant * np.exp((-x**2) / 2.0) )

z_score, _ = quad(normalProbabilityDensity, np.NINF, z)
print("Z Score = " + str(z_score))