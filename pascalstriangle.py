import numpy as np

A = [1]

def color(c):
	if c == '0':
		return "\33[01;31m0\33[m"
	else:
		return " "

while True:
	A = np.convolve(A, [1, 1])
	coloredoutput = ""
	for i in str([s % 7 for s in A]):
		coloredoutput += color(i)
	print(coloredoutput)
