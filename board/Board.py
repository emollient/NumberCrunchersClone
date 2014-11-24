import pygame
#from pygame import Rect
#from pygame import Color
#from pygame import draw

class Board:
	def __init__(self, topLeft, cellSize, width, height, surface):
		self.topLeft = topLeft
		self.cellSize = cellSize
		self.surface = surface
		self.width = width
		self.height = height
		self.rows = self.height / self.cellSize
		self.cols = self.width / self.cellSize
		self.boardArray = []
		for x in xrange(0, self.rows):
			self.boardArray.append([])
			for y in xrange(0, self.cols):
				self.boardArray[x].append([])

	#Sets a game object as the player
	def addPlayer(self, gameObject, x, y):
		self.player = gameObject;
		self.addGameObject(gameObject, x, y)

	#Adds an object to the board at a given position
	def addGameObject(self, gameObject, x, y):
		self.setPosition(gameObject, x, y)

		self.boardArray[x][y].append(gameObject)

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

		screenX = (x * self.cellSize)
		screenY = (y * self.cellSize)

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
		bgColor = pygame.Color(16, 64, 222)
		black = pygame.Color(0,0,0)
		pygame.draw.rect(self.surface, bgColor, background, 0)

		# draw grid lines
		for x in xrange(0, self.cols):
			pygame.draw.line(self.surface, black, (x * self.cellSize, originY), (x * self.cellSize, originY + self.height), 2)
		for y in xrange(0, self.rows):
			pygame.draw.line(self.surface, black, (originX, y * self.cellSize), (originX + self.width, y * self.cellSize), 2)

		# Draw everything stored on the board
		for x in xrange(0, self.rows):
			for y in xrange(0, self.cols):
				for i in xrange(0, len(self.boardArray[x][y])):
					self.boardArray[x][y][i].draw()

	# TODO: get the immediate neighbors for a given cell, should be useful for enemy AI
	def getNeighbors(self, xIndex, yIndex):
		pass
