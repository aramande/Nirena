from nirena.util.direction import Direction
import unittest

class DirectionTest(unittest.TestCase):
	def testOverflow(self):
		self.assertEqual(-179.0, Direction(181.0).get())
		
	def testUnderflow(self):
		self.assertEqual(179.0, Direction(-181.0).get())
	
	def testMiddleflow(self):
		self.assertEqual(91.5, Direction(91.5).get())

	def testAddSumOverflow(self):
		self.assertEqual(-172.5, (Direction(94.4) + Direction(93.1)).get())
		
	def testAddNegatives(self):
		first = Direction(-94.4)
		second = Direction(93.1)
		expected = -1.3
		diff = abs((first+second).get() - expected)
		delta = 0.01
		self.assertTrue(diff < delta, "difference(%s) is not less that delta(%s)" % (diff, delta))
		
	def testSubNegatives(self):
		first = Direction(-94.4)
		second = Direction(93.1)
		expected = 172.5
		diff = abs((first-second).get() - expected)
		delta = 0.01
		self.assertTrue(diff < delta, "difference(%s) is not less that delta(%s)" % (diff, delta))
		