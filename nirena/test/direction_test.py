from nirena.util.direction import Direction
import unittest

class DirectionTest(unittest.TestCase):
	def testOverflow(self):
		self.assertEqual(-1.0, Direction(181.0).get())
		
	def testUnderflow(self):
		self.assertEqual(1.0, Direction(-181.0).get())
	
	def testMiddleflow(self):
		self.assertEqual(91.5, Direction(91.5).get())
