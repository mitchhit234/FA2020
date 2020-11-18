#!/usr/bin/python3
import numpy as np

n = input("Sample size: ")
x = input("Number of desireable outcome: ")
p = input("P value: ")

n = float(n)
x = float(x)
p = float(p)

p_hat = x / n

test_statistic = (p_hat - p) / np.sqrt((p * (1 - p)) / n)

print(test_statistic)