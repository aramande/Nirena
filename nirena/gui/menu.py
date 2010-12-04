from nirena.gui import Container
class Menu(Container):
	""" A container for forming menues with rows and/or columns of components. Remember, a container is a component to. """
	
	LEFT, CENTER, RIGHT = 0, 1, 2 # Alignment constants
	
	
	def __init__(self, point, size):
		""" 
		@param point: Expects an object of type C{Point(x, y)}
		@param size: Expects a tuple of two numbers, preferably integers """
		pass
	
	def addComponent(self, component, newrow=True, align=LEFT):
		""" Add a new component to the menu. Position is overridden here.
		
		@param component: Expects any object type of the gui package
		@param newrow: False to stay on the same row, True to put next component on the next row 
		@param align: Alignment within the column, values consist of C{Menu.LEFT}, C{Menu.CENTER} or C{Menu.RIGHT} """
		pass
		
	def addListener(self, listener):
		""" Add an event listener to this container area, active whenever the container is shown.
		
		@param listener: Expects any listener from the event package """
		pass
	
	def show(self):
		""" Calls C{show(self)} in all component objects in storage. """
		pass
		
	def hide(self):
		""" Calls C{hide(self)} in all component objects in storage and inactivates any active listener. """
		pass
		