from nirena.util.resources import db_path
#from nirena.game.world import World

worldmap = open(db_path("map.txt"), 'r+')
objects = open(db_path("object.txt"), 'r+')

def loadMap():
	#world = World()
	world = None
	return world

def getObject(id):
	obj = None
	size = 5
	if id > 0: #Checking against negative id's
		for line in objects.readlines():
			item = line.strip().split('\t')
			if int(item[0]) == id:
				obj = [0]*size
				obj[0] = int(item[0])
				obj[1] = item[1]
				obj[2] = float(item[2])
				obj[3] = float(item[3])
				obj[4] = float(item[4])
			elif int(item[0]) > id:
				break
	return obj