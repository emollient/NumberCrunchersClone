import pygame
#from pygame import Rect
#from pygame import Color
#from pygame import draw

class Board:
	def __init__(self, cellSize, width, height, surface):
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
		background = pygame.Rect(0, 0, self.width, self.height)
		bgColor = pygame.Color(16, 64, 222)
		pygame.draw.rect(self.surface, bgColor, background, 0)

		# draw grid lines
		for x in xrange(0, self.rows):
			pygame.draw.line(self.surface, black, (x * self.cellSize, 0), (x * self.cellSize, self.height), 2)
		for y in xrange(0, self.cols):
			pygame.draw.line(self.surface, black, (0, y * self.cellSize), (this.width, y * self.cellSize), 2)
				
	# TODO: get the immediate neighbors for a given cell, should be useful for enemy AI
	def getNeighbors(self, xIndex, yIndex):
		pass
