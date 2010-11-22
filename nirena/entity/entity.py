from nirena.util.resources import load_image, get_class
class Entity:
	def __init__(self, sprite, friction, *rect):
		"""
			Creates an entity with their own sprite and position/size on the screen.
			rect can either be four floatingpoint numbers, or a pygame.Rect
			Rect order: x, y, width, height
		"""
		if friction < 0.0:
			raise ValueError("Friction cannot be negative")
		
		self.pos = [0,0]
		self.size = [0,0]
		self.setSprite(sprite)
		self.friction = friction
		self.setPosition(*rect)
			
	def setSprite(self, sprite):
		if sprite == "" or sprite == None:
			raise ValueError("Sprite has to have a value")
		self.sprite = load_image(sprite)
		self.size[0] = self.sprite.get_rect().width
		self.size[1] = self.sprite.get_rect().height
	
	def setPosition(self, *rect):
		if len(rect) > 4:
			raise ValueError("Can't have more than 4 values of rect")
		if len(rect) == 3:
			raise ValueError("Can't have 3 values of rect")
			
		if len(rect) == 1 and get_class(rect[0]) == 'Rect':
			self.pos[0] = rect[0].left
			self.pos[1] = rect[0].top
		elif len(rect) == 2 or len(rect) == 4:
			self.pos[0] = rect[0]
			self.pos[1] = rect[1]
	
	def draw(self):
		pass
