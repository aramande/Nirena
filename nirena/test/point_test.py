from nirena.util.point import Point
import unittest

class PointTest(unittest.TestCase):
	def testIllegalNumberOfArguments(self):
		self.assertRaises(TypeError, Point, 4)
		
	def testAdd(self):
		self.assertEqual((5,6), (Point(2,3)+Point(3,3)).get())
		
	def testSub(self):
		self.assertEqual((-1,0), (Point(2,3)-Point(3,3)).get())