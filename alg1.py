import numpy as np


def take_norm_vector(flat):
	x = flat.index('x')
	y = flat.index('y')
	z = flat.index('z')
	norm_vector = list(map(float, [flat[:x], flat[x + 1: y], flat[y + 1: z]]))
	return norm_vector


def solve(flat1, flat2, dot):
	n1 = take_norm_vector(flat1)
	n2 = take_norm_vector(flat2)
	norm_vector = list(np.cross(n1, n2))
	result = '{}(x - {}) + {}(y - {}) + {}(z - {}) = 0'.format(
		norm_vector[0], dot[0], norm_vector[1], dot[1], norm_vector[2], dot[2])
	result = result.replace('- -', '+ ')
	result = result.replace('+ -', '- ')
	return result


def main():
	flat1 = '4x+1y-3z+13=0'
	flat2 = '1x-2y+1z-11=0'
	dot = [-3, 2, 5]
	result = solve(flat1, flat2, dot)
	print(result)


if __name__ == '__main__':
	main()
