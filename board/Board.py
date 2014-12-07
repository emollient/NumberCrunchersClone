import pygame
#from pygame import Rect
#from pygame import Color
#from pygame import draw

class Board:
	def __init__(self, topLeft, width, height, surface):
		self.topLeft = topLeft
		self.surface = surface
		self.width = width
		self.height = height

		self.rows = 5
		self.cols = 6

		self.cellWidth = width/self.cols;
		self.cellHeight = height / self.rows;

		self.boardArray = []
		for x in range(0, self.cols):
			self.boardArray.append([])
			for y in range(0, self.rows):
				self.boardArray[x].append([])

	#Sets a game object as the player
	def addPlayer(self, gameObject, x, y):
		self.player = gameObject;
		self.addGameObject(gameObject, x, y)

	#Adds an object to the board at a given position
	def addGameObject(self, gameObject, x, y):
		self.setPosition(gameObject, x, y)

		self.boardArray[x][y].append(gameObject)

	#Adds an object to the board assuming the object knows where it should be already
	def addMunchable(self, gameObject):
		boardCoords = gameObject.get_boardCoords();
		x = boardCoords['x']
		y = boardCoords['y']

		self.addGameObject(gameObject, x, y)

	def setPosition(self, gameObject, x, y):
		if x > self.cols or y > self.rows or x < 0 or y < 0:
			print "Position " + str(x) + " : " + str(y) +" off board"
			return

		#Calculate screen positon
		screenPos = self.calcScreenPos(x, y);

		#Set the game object's positions
		gameObject.set_boardCoords(x, y)
		gameObject.set_screenPos(screenPos['x'], screenPos['y'])

	def calcScreenPos(self, x, y):
		screenPos = {'x': 0, 'y': 0}

		screenX = (x * self.cellWidth)
		screenY = (y * self.cellHeight)

		screenPos['x'] = screenX
		screenPos['y'] = screenY

		return screenPos

	def events(self, event):

		#Get player pos
		playerPos = self.player.get_boardCoords()

		if event.type == pygame.KEYDOWN:
			# Up
			if event.key == 119 or event.key == 273:
				if playerPos['y'] > 0:
					self.setPosition(self.player, playerPos['x'], playerPos['y'] - 1)

			# Left
			elif event.key == 97 or event.key == 276:
				if playerPos['x'] > 0:
					self.setPosition(self.player, playerPos['x'] - 1, playerPos['y'])

			# Down
			elif event.key == 115 or event.key == 274:
				if playerPos['y'] < self.rows - 1:
					self.setPosition(self.player, playerPos['x'], playerPos['y'] + 1)

			# Right
			elif event.key == 100 or event.key == 275:
				if playerPos['x']  < self.cols - 1:
					self.setPosition(self.player, playerPos['x'] + 1, playerPos['y'])

		self.player.events(event)

	def draw(self):
		# draw the background, just a rectangle for now
		# to save memory we could maybe use screen.fill(color)
		originX = self.topLeft['x']
		originY = self.topLeft['y']
		background = pygame.Rect(originX, originY, self.width, self.height)
		bgColor = pygame.Color(0, 0, 0)
		lineColor = pygame.Color(255,0,255)
		pygame.draw.rect(self.surface, bgColor, background, 0)

		# draw grid lines
		for x in xrange(0, self.cols + 1):
			pygame.draw.line(self.surface, lineColor, ((x * self.cellWidth) + originX, originY), ((x * self.cellWidth) + originX, originY + self.height), 2)
		for y in xrange(0, self.rows + 1):
			pygame.draw.line(self.surface, lineColor, (originX, (y * self.cellHeight) + originY), (originX + self.width, (y * self.cellHeight) + originY), 2)

		# Draw everything stored on the board
		for x in xrange(0, self.cols):
			for y in xrange(0, self.rows):
				for i in xrange(0, len(self.boardArray[x][y])):
					self.boardArray[x][y][i].draw()

	# TODO: get the immediate neighbors for a given cell, should be useful for enemy AI
	def getNeighbors(self, xIndex, yIndex):
		pass
