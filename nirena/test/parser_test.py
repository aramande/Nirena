import nirena.util.parser
import unittest

class ParserTest(unittest.TestCase):
	
	def setUp(self):
		unittest.TestCase.setUp(self)
		self.parser = Parser()
		
	def testGetObject(self):
		self.assertEqual([1, "player.png", 10.0, 10.0, 0.0], self.parser.getObject(1))
		
	def testNegativeObject(self):
		self.assertEqual(None, self.parser.getObject(-1))
		