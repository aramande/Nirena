from nirena.entity.entity import Entity
from pygame import Rect
import unittest

class EntityTest(unittest.TestCase):
	def testCoords(self):
		Entity("player.png", 0.0, 0.0, None, 1, 2)
	
	def testRect(self):
		Entity("player.png", 0.0, 0.0, None, Rect(1, 2, 3, 4))
	
	def testTooManyCoords(self):
		self.assertRaises(ValueError, Entity, "player.png", 0.0, 0.0, None, 1, 2, 3, 4, 5)
		
	def testOddNumberCoords(self):
		self.assertRaises(ValueError, Entity, "player.png", 0.0, 0.0, None, 1, 2, 3)
		
	def testNoCoords(self):
		Entity("player.png", 0.0, 0.0, None)
		
	def testNullCoords(self):
		Entity("player.png", 0.0, 0.0, None, None)
		
	def testNoSprite(self):
		self.assertRaises(ValueError, Entity, "", 0.0, 0.0, None, 1, 2, 3, 4)
		
	def testNullSprite(self):
		self.assertRaises(ValueError, Entity, None, 0.0, 0.0, None, 1, 2, 3, 4)
		
	def testNegativeFriction(self):
		self.assertRaises(ValueError, Entity, "player.png", -0.1, 0.0, None, 1, 2, 3, 4)
		
	def testNegativeMass(self):
		self.assertRaises(ValueError, Entity, "player.png", 0.0, -0.1, None, 1, 2, 3, 4)
	