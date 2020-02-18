import numpy as np
import re


def take_norm_vector(data):
	pat = r'([+-]?\d*)x([+-]?\d*)y([+-]?\d*)z[+-]?\d*=0'
	flat = re.search(pat, data)
	if not flat:
		raise ValueError('Incorrect input, check equation')
	norm_vector = []
	# get coordinates of normal vector from regex
	for i in flat.groups():
		if i == '+' or i == '':
			norm_vector.append(1.0)
		elif i == '-':
			norm_vector.append(-1.0)
		else:
			norm_vector.append(float(i))
	return norm_vector


def solve(flat1, flat2, dot):
	# get two normal vectors
	n1 = take_norm_vector(flat1)
	n2 = take_norm_vector(flat2)
	# multiply them to get normal vector for our flat
	norm_vector = list(np.cross(n1, n2))
	d = 0
	for i in range(len(norm_vector)):
		d += norm_vector[i] * -1 * dot[i]
	result = norm_vector + [d,]

	return result
