class Event:
	""" Contains information about what happened with the mouse during the event """
	def __init__(self, key, mod=None, unicode=None):
		""" 		
		@param  key
		@param  mod
		@param  unicode """
		pass
	
	def getKey(self):
		return 0
	
	def getModifier(self):
		return 0
	
	def getUnicode(self):
		return Point(1,1)
		
	def timeSinceLastEvent(self):
		""" Not sure how to implement this, will need to have a kind of storage for the time of the last event """
		pass

class Listener:
	""" Listens for the players mouse actions """
	def __init__(self):
		pass
		
	def listen(self, event=None):
		""" Calls all stored code when the relevant 'event' is active. 
		
		@param  event  Event object to pull information from, if None, nothing happened this frame """
		pass

	def onKeyDown(self, code, keys=None)
		""" Stores 'code' to be called once when the user pushes down one of 'keys'
		then calls the code with a keyboard.Event object as argument.
		
		@param  code  Expects a function that takes one argument for the keyboard.Event object 
		@param  keys  A list of pygame keycodes; if an entry is a list or tuple, first value 
		should be a modifier and second a key; if None, code will always be called when a key is pushed """
		pass
		
	def whileKeyPressed(self, code, keys=None):
		""" Stores 'code' to be called every frame from when the user 
		pushes down one of 'keys' until the user releases the same key
		then calls the code with a keyboard.Event object as argument.
		
		@param  code  Expects a function that takes one argument for the keyboard.Event object 
		@param  keys  A list of pygame keycodes; if an entry is a list or tuple, first value
		should be a modifier and second a key; if None, code will always be called while a key is being pushed """
	
	def onKeyUp(self, code, keys=None)
		""" Stores 'code' to be called when the user releases a previously pressed key and 
		then calls the code with a mouse.Event object as argument.
		
		@param  code  Expects a function that takes one argument for the keyboard.Event object 
		@param  keys  A list of pygame keycodes; if an entry is a list or tuple, first value
		should be a modifier and second a key; if None, code will always be called when a key is released """
		pass
		
		