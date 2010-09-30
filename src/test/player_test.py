import player
import unittest

class PlayerStub(player.Player):
	def __init__(self):
		""" Made so that all dependencies upon other files and stuff wasn't needed """
		self.vely = 0;
		self.terminalVelocity = 8
		self.fall = True
		pass


class PlayerTest(unittest.TestCase):

	def setup(self):
		self.p = PlayerStub()

	def testVerticalVelocity(self):
		self.setup()
		
		self.assertEqual(self.p.verticalVelocity(9.80665, 0.5), 4.9)
		self.assertEqual(self.p.verticalVelocity(-5.0, 7.0), -35.0)
		self.assertEqual(self.p.verticalVelocity(-10.0+1.0-1.0, 10.0), -100.0)
		self.assertEqual(self.p.verticalVelocity(1.0-1.0, 10.0), 0.0)
		
		self.teardown()
	
	def testSpriteInMotion(self):
		self.setup()
		
		self.p.vely = 1.0;
		self.assertEqual(self.p.verticalVelocity(-0.4+0.2-0.0, 1.0), 0.8)
		
		self.teardown()
		
	def testJumpingArc(self):
		self.setup()
		
		self.p.vely = 0.0;
		vely = self.p.verticalVelocity(-0.4+0.02-0.0, 1.0)
		self.assertEqual(vely, -0.38)
		last = -0.38
		while vely < 4:
			self.p.vely = last;
			vely = self.p.verticalVelocity(0.02-0.0, 1.0)
			self.assertEqual(vely, round(last + 0.02,2))
			last += 0.02
		
		self.teardown()
		
	def testNegativeTime(self):
		self.setup()
		
		self.assertRaises(ValueError,self.p.verticalVelocity, 1, -1)
		self.assertRaises(ValueError,self.p.verticalVelocity, 5, -6.2)
		
		self.teardown()
		
	def teardown(self):
		pass
	