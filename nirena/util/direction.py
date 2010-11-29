#14:33-16:00
class Direction:
	def __init__(self, degree):
		if degree < -180:
			degree += 360
		elif degree > 180:
			degree -= 360
		self._dir = degree

	def __add__(self, other):
		"Addition between direction objects, good for figuring out the result of an additional force."
		dir = self._dir + other._dir
		return Direction(dir)

	def __sub__(self, other):
		"Subtraction between direction objects, good for figuring out the result of removing a force."
		dir = self._dir - other._dir
		return Direction(dir)
		
	def get(self):
		"Returns the current direction"
		return self._dir
		
	def __float__(self):
		"Synonym to get()"
		return self._dir