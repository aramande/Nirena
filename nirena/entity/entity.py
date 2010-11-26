from nirena.util.resources import load_image, get_class
class Entity:
	def __init__(self, sprite):
		"""
			Creates an entity with their own sprite and position/size on the screen.
			rect can either be four floatingpoint numbers, or a pygame.Rect
			Rect order: x, y, width, height
		"""
		self.pos = [0,0]
		self.size = [0,0]
		self.setSprite(sprite)
		#self.setPosition(*point)
			
	def setSprite(self, sprite):
		if sprite == "" or sprite == None:
			raise ValueError("Sprite has to have a value")
		self.sprite = load_image(sprite)
		self.size[0] = self.sprite.get_rect().width
		self.size[1] = self.sprite.get_rect().height
	"""
	def setPosition(self, *point):
		if len(point) > 4:
			raise ValueError("Can't have more than 4 values of rect")
		if len(point) == 3:
			raise ValueError("Can't have 3 values of rect")
			
		if len(point) == 1 and get_class(point[0]) == 'Rect':
			self.pos[0] = point[0].left
			self.pos[1] = point[0].top
		elif len(point) == 2 or len(point) == 4:
			self.pos[0] = point[0]
			self.pos[1] = point[1]
	"""
	def draw(self):
		pass
