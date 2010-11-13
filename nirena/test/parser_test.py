from nirena.util.parser import Parser
import unittest

class ParserTest(unittest.TestCase):
	
	def setUp(self):
		unittest.TestCase.setUp(self)
		self.parser = Parser()
		
	def testGetObject(self):
		#Database specific test. 
		#Change this if the database changes.
		self.assertEqual([1, "player.png", 10.0, 10.0, 0.0], self.parser.getObject(1))
		
	def testNegativeObject(self):
		self.assertEqual(None, self.parser.getObject(-1))
	
	def testNonExistantObject(self):
		#Database specific test. 
		#Change this if the database changes.
		self.assertEqual(None, self.parser.getObject(123874))
		
	def tearDown(self):
		unittest.TestCase.tearDown(self)
		del(self.parser)