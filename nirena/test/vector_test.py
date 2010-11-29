from nirena.util.point import Point
from nirena.util.vector import Vector
from nirena.util.velocity import Velocity
from nirena.util.direction import Direction
import unittest
import math

class VectorTest(unittest.TestCase):
	def testNullPoints1(self):
		self.assertRaises(ValueError, Vector, None, Point(1, 2))
		
	def testNullPoints2(self):
		self.assertRaises(ValueError, Vector, Point(1, 2), None)
		
	def testNotPoints1(self):
		Vector((1,3),(2,4))
		
	def testToVelocity(self):
		vector = Vector(Point(0,0), Point(1,1))
		velocity = Velocity(math.sqrt(2), Direction(45.0))
		self.assertEquals(velocity.getDirection().get(), vector.toVelocity().getDirection().get())
		self.assertEquals(velocity.getDistance(), vector.toVelocity().getDistance())
		
	def testToVelocity2(self):
		vector = Vector(Point(1,1), Point(2,2))
		velocity = Velocity(math.sqrt(2), Direction(45.0))
		self.assertEquals(velocity.getDirection().get(), vector.toVelocity().getDirection().get())
		self.assertEquals(velocity.getDistance(), vector.toVelocity().getDistance())