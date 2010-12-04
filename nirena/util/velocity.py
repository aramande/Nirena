#17:19-19:48
from nirena.util.point import Point
from nirena.util.vector import Vector
from nirena.util.direction import Direction
import math

class Velocity:
	def __init__(self, dist=0.0, degree=Direction(0.0)):
		if dist == None or degree == None:
			raise TypeError("Velocity does not accept None values, please use the defaults instead")
		
		self._dist = dist
		self._degree = degree
				
	def __add__(self, other):
		if other == None:
			raise ValueError("The other point needs to have a value")
		v = self.toVector()
		w = other.toVector()
		return Velocity(v+w)
		
	def __sub__(self, other):
		if other == None:
			raise ValueError("The other point needs to have a value")
		v = self.toVector()
		w = other.toVector()
		return Velocity(v-w)
		
	def getNextPosition(self, pos, delta):
		"""
		@param pos: Last known position
		@param delta: Time since last frame, in milliseconds
		"""
		dist = self._dist * delta
		x = dist * math.cos(self._toRad(self._degree))
		y = dist * math.sin(self._toRad(self._degree))
		
		return pos + Point(x, y)

	def getDistance(self):
		return self._dist
	
	def getDirection(self):
		return self._degree
	
	def toVector(self):
		x = self._dist * math.cos(self._toRad(self._degree))
		y = self._dist * math.sin(self._toRad(self._degree))
		return Vector(Point(0,0), Point(x, y))
	
	def _toRad(self, deg):
		return deg.get() * (math.pi/180)
