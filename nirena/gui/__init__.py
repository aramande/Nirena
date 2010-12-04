class Gui:
	""" A basic 'window' in the game """
	def __init__(self, component):
		""" 
		@param component: Expects one of any Gui object, such as a Container or Component, needs to have a C{show(self)} and a C{hide(self)} function """
		pass
		
	def addListener(self, listener):
		""" Add an event listener to this object, active whenever the container is shown.
		
		@note: A Gui object has no area to click in or move over, so C{mouse.Listener} and any derivatives won't work. 
		@param listener: Expects any listener from the event package """
		pass
	
	def show(self):
		""" Run the show function in all the components contained within the Gui every frame. """
		pass
		
	def hide(self):
		""" Calls C{hide(self)} in all component objects in storage and inactivates any active listener. """

class Component:
	""" A single component in a grafical interface. """
	pass

class Container(Component):
	""" A container of multiple components. """
	pass
	