import src.player
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
		
		#Good values:
		self.assertEqual(self.p.verticalVelocity(9.80665, 0.5), 4.9)
		self.assertEqual(self.p.verticalVelocity(-10.0+1.0-1.0, 10.0), -100.0)
		self.assertEqual(self.p.verticalVelocity(1.0-1.0, 10.0), 0.0)
		
		#Sprite in motion:
		self.p.vely = 1.0;
		self.assertEqual(self.p.verticalVelocity(-0.4+0.2-0.0, 1.0), 0.8)
		
		#Jumping arc:
		self.p.vely = 0.0;
		vely = self.p.verticalVelocity(-0.4+0.02-0.0, 1.0)
		self.assertEqual(vely, -0.38)
		last = -0.38
		while vely < 4:
			self.p.vely = last;
			vely = self.p.verticalVelocity(0.02-0.0, 1.0)
			self.assertEqual(vely, round(last + 0.02,2))
			last += 0.02
		
		
		#Bad values (Negative or no time):
		self.assertRaises(ValueError,self.p.verticalVelocity, 1, -1)
		self.assertRaises(ValueError,self.p.verticalVelocity, 9.80665, 0)
		self.teardown()
		
	def teardown(self):
		pass
	