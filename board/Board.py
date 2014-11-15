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
				self.boardArray[x].append(None)

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
				
	# TODO: get the immediate neighbors for a given cell, should be useful for enemy AI
	def getNeighbors(self, xIndex, yIndex):
		pass
