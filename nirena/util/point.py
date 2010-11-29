#16:00-16:30
class Point:
	def __init__(self, xy, y = None):
		if y == None:
			try:
				self._x, self._y = xy
			except TypeError:
				raise TypeError("Need two arguments, or one tuple with two values.")
		elif xy != None:
			self._x = xy
			self._y = y
		else:
			raise TypeError("Need two arguments, or one tuple with two values.")
	
	def __add__(self, other):
		x = self._x + other._x
		y = self._y + other._y
		return Point(x, y)
	
	def __sub__(self, other):
		x = self._x - other._x
		y = self._y - other._y
		return Point(x, y)
	
	def get(self):
		return self._x, self._y
	
	def getX(self):
		return self._x
	
	def getY(self):
		return self._y