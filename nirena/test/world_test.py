from nirena.game.world import World
from nirena.entity.entity import Entity
import unittest

class EntityStub(Entity):
	def __init__(self):
		pass
	def setPosition(self, position):
		pass

class WorldTest(unittest.TestCase):
	def testValidConstructor(self):
		World("player.png", EntityStub(), (1,1))
	
	def testNoBackground(self):
		self.assertRaises(ValueError, World, "", None, None)
	
	def testNullBackground(self):
		self.assertRaises(ValueError, World, None, None, None)
		
	def setUp(self):
		unittest.TestCase.setUp(self)
		self.w = World("player.png", EntityStub(), (1,1))
		
	def testAddNoEntity(self):
		self.assertRaises(ValueError, self.w.addEntity, None, (1,1))
		
	def testAddNoPosition(self):
		self.assertRaises(ValueError, self.w.addEntity, EntityStub(), None)
		
	def testAddNotEqual(self):
		self.assertRaises(IndexError, self.w.addEntity, [EntityStub()], [(1,2), (2,1)])
		
	def testAddNotEqual2(self):
		self.assertRaises(IndexError, self.w.addEntity, [EntityStub(), EntityStub(), EntityStub()], [(1,2), (2,1)])
		
	def tearDown(self):
		unittest.TestCase.tearDown(self)
		del self.w