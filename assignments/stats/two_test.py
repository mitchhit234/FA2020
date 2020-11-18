#!/usr/bin/python3
import numpy as np


x1 = float(input("Mean of sample 1: "))
s1 = float(input("Deviation of sample 1: "))
n1 = float(input("Size of sample 1: "))
x2 = float(input("Mean of sample 2: "))
s2 = float(input("Deviation of sample 2: "))
n2 = float(input("Size of sample 2: "))

assumed_equal = input("Variances assumed equal? ")

if assumed_equal == "y":

	pooled_variance = (((n1 - 1) * s1**2) + ((n2 - 1) * s2**2)) / (n1 + n2 - 2)

	test_statistic = (x1 - x2) / (np.sqrt(pooled_variance) * np.sqrt((1 / n1) + (1 / n2)))

	print("Pooled Variance (unsquared): " + str(np.sqrt(pooled_variance)))



else:

	test_statistic = (x1 - x2) / np.sqrt((s1**2 / n1) + (s2**2 / n2))

	top_d = ((s1**2 / n1) + (s2**2 / n2))**2

	d = top_d / (((s1**2 / n1)**2 / (n1-1)) + ((s2**2 / n2)**2 / (n2-1)))

	print("Degrees of Freedom: " + str(d))


print("Test Statistic: " + str(test_statistic))