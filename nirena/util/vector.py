#16:30-17:20
from nirena.util.direction import Direction
from nirena.util.point import Point
from nirena import util
import math

class Vector:
	def __init__(self, pointA, pointB):
		if pointA == None or pointB == None:
			raise ValueError("The points need to have values")
		
		self._a = self._verifyPoint(pointA)
		self._b = self._verifyPoint(pointB)
			
	def _verifyPoint(self, point):
		try:
			point.get()
			return point
		except AttributeError:
			try:
				if len(point) >= 2:
					return Point(point[0], point[1])
			except TypeError:
				raise AttributeError("Expected object of type Point or tuple")
				
	def __add__(self, other):
		if other == None:
			raise ValueError("The other point need to have a value")
		a = self._a + other._a
		b = self._b + other._b
		return Vector(a, b)
		
	def __sub__(self, other):
		if other == None:
			raise ValueError("The other point need to have a value")
		a = self._a - other._a
		b = self._b - other._b
		return Vector(a, b)
				
	def getPointA(self):
		return self._a
		
	def getPointB(self):
		return self._b
	
	def toVelocity(self):
		p = self._b - self._a
		distance = math.sqrt(math.pow(p.getX(), 2)+ math.pow(p.getY(), 2))
		direction = Direction(self._toDegree(self._getDirection(p.getX(), p.getY())))
		return util.velocity.Velocity(distance, direction)
		
	def _toDegree(self, rad):
		return rad * (180/math.pi)
		
	def _getDirection(self, x, y):
		if x == 0.0: 
			if y == 0.0:
				return 0
			elif y < 0.0:
				return -(math.pi/2)
			elif y > 0.0:
				return math.pi/2
		if x < 0.0:
			if y >= 0.0:
				return math.atan(y/x) + math.pi
			if y < 0.0:
				return math.atan(y/x) - math.pi
		if x > 0:
			return math.atan(y/x)
