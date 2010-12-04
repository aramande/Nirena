""" This is the active event generator. The module name is intended as a pun: I{If someone is shouting, anyone who's listening is bound to hear them}. """		


def shout(self):
	""" Runs once every frame. Loops through all Entities (or Gui if shown) objects, running all the active listeners C{listen} function in the progress, sending the argument C{None} if no event happened this frame """
	pass
