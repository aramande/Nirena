def _getClass(obj):
	return obj.__class__.__name__

class Entity:
	def __init__(self, sprite, friction, mass, rotation, *rect):
		"""
			Creates an entity with their own sprite and position/size on the screen.
			rect can either be four floatingpoint numbers, or a pygame.Rect
			Rect order: x, y, width, height
		"""
		if friction < 0.0:
			raise ValueError("Friction cannot be negative")
		if mass < 0.0:
			raise ValueError("Mass cannot be negative")
		if rect[0] == None or len(rect) == 0:
			raise ValueError("Rect has to have a value")
		if sprite == "" or sprite == None:
			raise ValueError("Sprite has to have a value")
		if len(rect) > 4:
			raise ValueError("Can't have more than 4 values of rect")
		if len(rect) == 3:
			raise ValueError("Can't have 3 values of rect")
		self.pos = [0,0]
		self.size = [0,0]
		if len(rect) == 1 and _getClass(rect[0]) == 'Rect':
			if rect[0].width < 0 or rect[0].height < 0:
				raise ValueError("Weight and/or Height cannot be negative")
			self.pos[0] = rect[0].left
			self.pos[1] = rect[0].top
			self.size[0] = rect[0].width
			self.size[1] = rect[0].height
		elif len(rect) == 4:
			if rect[2] < 0 or rect[2] < 0:
				raise ValueError("Weight and/or Height cannot be negative")
			self.pos[0] = rect[0]
			self.pos[1] = rect[1]
			self.size[0] = rect[2]
			self.size[1] = rect[3]
			
	def draw():
		pass
