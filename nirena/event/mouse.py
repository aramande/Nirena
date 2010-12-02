from nirena.util.point import Point
class Event:
	""" Contains information about what happened with the mouse during the event """
	def __init__(self, button, point, rel=None):
		""" 
		@param  button  An integer explaining what button the user used, 0 and None means mousemotion
		@param  point  Expects a point object or a tuple with two numerical values 
		@param  rel  A redirected value from the mousemotion pygame event """
		pass
	
	def getInfo(self, key=None):
		""" Returns information about the event that happened.
		
		@param  key  Dictionary key, if None, all values will be returned
		@return Value of the key in the dictionary, or all values if no key was given """
		return 0, Point(1,1), 0
		
	def timeSinceLastEvent(self):
		""" Not sure how to implement this, will need to have a kind of storage for the time of the last event 
		
		@return Delta time between events in milliseconds """
		return 1

class Listener:
	""" Listens for the players mouse actions """
	def __init__(self):
		pass
		
	def listen(self, event=None):
		""" Calls all stored code when the relevant 'event' is active. 
		
		@param  event  Event object to pull information from, if None, nothing happened this frame """
		pass

	def onMovement(self, code, buttons=None)
		""" Stores 'code' to be called when the user moves his mouse and 
		then calls the code with a mouse.Event object as argument.
		
		@param  code  Expects a function that takes one argument for the mouse.Event object
		@param  buttons  Collection of buttons that must be held down, None for none.. obviously. """
		pass
		
	def onButtonDown(self, code, button=None):
		""" Stores 'code' to be called when the user clicks a button on the mouse and 
		then calls the code with a mouse.Event object as argument.
		
		@param  code  Expects a function that takes one argument for the mouse.Event object
		@param  button  The identification of the button on the mouse, if None, code is run every time the user clicks """
		pass
		
	def whileButtonPressed(self, code, button=None):
		""" Stores 'code' to be called every frame when the user holds a button on the mouse and 
		then calls the code with a mouse.Event object as argument.
		
		@param  code  Expects a function that takes one argument for the mouse.Event object 
		@param  button  The identification of the button on the mouse, if None, code is run every frame the user clicks any mousebutton """
		pass
		
	def onButtonUp(self, code, button=None):
		""" Stores 'code' to be called when the user releases a pressed button on the mouse and 
		then calls the code with a mouse.Event object as argument.
		
		@param  code  Expects a function that takes one argument for the mouse.Event object 
		@param  button  The identification of the button on the mouse, if None, code is run every time the user releases a mousebutton"""
		pass
