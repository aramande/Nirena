from nirena.util.point import Point
from nirena.util.vector import Vector
from nirena.util.velocity import Velocity
from nirena.util.direction import Direction
import math
import unittest

class VelocityTest(unittest.TestCase):
	def testNullDir(self):
		self.assertRaises(TypeError, Velocity, 2.2, None)
		
	def testNullDist(self):
		self.assertRaises(TypeError, Velocity, None, Direction(23.1))
		
	def testToVector(self):
		vector = Vector(Point(0,0), Point(1,1))
		velocity = Velocity(math.sqrt(2), Direction(45.0))
		first = vector.getPointA().getX()
		second = velocity.toVector().getPointA().getX()
		diff = abs(first-second)
		delta = 0.01
		self.assertTrue(diff < delta, "difference(%s) is not less that delta(%s)" % (diff, delta))
		
	def testToVector2(self):
		vector = Vector(Point(0,0), Point(1,1))
		velocity = Velocity(math.sqrt(2), Direction(45.0))
		first = vector.getPointA().getY()
		second = velocity.toVector().getPointA().getY()
		diff = abs(first-second)
		delta = 0.01
		self.assertTrue(diff < delta, "difference(%s) is not less that delta(%s)" % (diff, delta))