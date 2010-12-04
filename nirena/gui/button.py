from nirena.gui import Component
class Button(Component):
	""" A button to put in a container or Gui """
	
	def __init__(self, point, size, text):
		""" 
		@param point: Sets the initial position of the button, depends on its container 
		@type point: L{Point}
		@param size: Sets a preferred size, actual size adjusts with textlength and depends on its container. 
		@type size: width, height
		@param text: Sets the text to be visible on the button
		@type text: C{str} """
		pass
	
	def addListener(self, listener):
		""" Add an event listener to this component area, active whenever the component is shown.
		
		@param listener: Adds this listener to the button
		@type listener: C{event.*.Listener} """
		pass
	
	def show(self):
		""" Calls C{show(self)} in all component objects in storage. """
		pass
		
	def hide(self):
		""" Anything that should happen after a button has been show will be run here. Listener will be inactive after this function is run.

		For example, you could choose to draw a square of background color over the button so that it's invisible. """
		pass
