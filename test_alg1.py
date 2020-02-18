import unittest
from alg1 import solve
from geometry import proj_point_on_plane, get_plane


class Test(unittest.TestCase):
	def test_solution(self):

		# solution from library
		plane1 = [4, 1, -3, 13]
		plane2 = [1, -2, 1, -11]
		dot = [-3, 2, 5]
		proj1 = proj_point_on_plane(plane1, dot)
		proj2 = proj_point_on_plane(plane2, dot)
		test = [round(i, 3) for i in get_plane(proj1, proj2, dot)]

		# my solution
		flat1 = '4x+y-3z+13=0'
		flat2 = 'x-2y+z-11=0'
		dot = [-3, 2, 5]
		result = solve(flat1, flat2, dot)
		result = [-1 * i for i in result]
		self.assertEqual(result, test)


if __name__ == '__main__':
	unittest.main()
