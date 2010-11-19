from nirena.util.parser import *
import unittest

class ParserTest(unittest.TestCase):
	
	def setUp(self):
		unittest.TestCase.setUp(self)
		
	def testGetObject(self):
		#Database specific test. 
		#Change this if the database changes.
		self.assertEqual([1, "player.png", 10.0, 10.0, 0.0], getObject(1))
		
	def testNegativeObject(self):
		self.assertEqual(None, getObject(-1))
	
	def testNonExistantObject(self):
		#Database specific test. 
		#Change this if the database changes.
		self.assertEqual(None, getObject(123874))
		
	def tearDown(self):
		unittest.TestCase.tearDown(self)