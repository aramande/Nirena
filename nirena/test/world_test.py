from nirena.world import World
from nirena.entity import Entity
import unittest

class EntityStub(Entity):
	def __init__(self):
		pass
		
	def show():
		pass

class WorldTest(unittest.TestCase):
	def testValidConstructor(self):
		World(EntityStub())
		
	def setUp(self):
		unittest.TestCase.setUp(self)
		self.w = World(EntityStub())
		
	def testAddNoEntity(self):
		self.assertRaises(ValueError, self.w.addEntity, None)
		
	def tearDown(self):
		unittest.TestCase.tearDown(self)
		del self.w