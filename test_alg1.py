import unittest
from alg1 import solve


class Test(unittest.TestCase):
	def test_solution(self):
		flat1 = '4x+y-3z+13=0'
		flat2 = 'x-2y+z-11=0'
		dot = [-3, 2, 5]
		result = solve(flat1, flat2, dot)
		self.assertEqual(result, '-5.0(x + 3) - 7.0(y - 2) - 9.0(z - 5) = 0')


if __name__ == '__main__':
	unittest.main()
