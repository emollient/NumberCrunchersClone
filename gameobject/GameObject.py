import pygame

class GameObject:
    def __init__(self, board, boardX, boardY):
        self.board = board
        self.screen = board.surface

        self.screenRect = {'x':0, 'y':0, 'width':0, 'height':0}
        self.boardCoords = {'x':boardX, 'y':boardY}

        #More primitive datastructure for blitting to screen
        self.drawRect = None

    #update our drawRect object whenever the screenRect object is changed
    def update_drawRect(self):
        centerX = (self.boardCoords['x'] * self.board.cellWidth) + self.board.topLeft['x'] + (self.board.cellWidth / 2) - (self.screenRect['width']/2)
        centerY = (self.boardCoords['y'] * self.board.cellHeight) + self.board.topLeft['y'] + (self.board.cellHeight / 2) - (self.screenRect['height']/2)
        self.drawRect = (centerX, centerY, self.screenRect['width'], self.screenRect['height'])

    def get_boardCoords(self):
        return self.boardCoords

    def get_screenRect(self):
        return self.screenRect

    def set_boardCoords(self, x, y):
        self.boardCoords['x'] = x
        self.boardCoords['y'] = y

    def set_screenPos(self, x, y):
        self.screenRect['x'] = x
        self.screenRect['y'] = y

        self.update_drawRect()

    #base draw function; should be overwritten by super classes
    def draw(self):
        pygame.draw(self.screen, (0, 129, 69), drawRect)

#player class
class Player(GameObject):

    def __init__(self, screen, boardX, boardY):
        GameObject.__init__(self, screen, boardX, boardY)

        self.points = 0

        self.leftImage = pygame.image.load("res/img/PlayerLeft.bmp")
        self.rightImage = pygame.image.load("res/img/PlayerRight.bmp")

        self.screenRect['width'] = self.leftImage.get_width()
        self.screenRect['height'] = self.leftImage.get_height()

        self.update_drawRect()

        #get our screenRect object into a form that the screen can blit with
        self.drawRect = (self.screenRect['x'], self.screenRect['y'], self.screenRect['width'], self.screenRect['height'])

        # State for which way to face; 0 is left, 1 is right
        self.state = 0

    def get_points(self):
        return self.points

    def add_points(self, points):
        self.points += points

    #This should be moved to the board class
    def events(self, event):
        # Up
        #if event.key == 119 or event.key == 273:

        # Left
        if event.key == 97 or event.key == 276:
            self.state = 0

        # Down
        #elif event.key == 115 or event.key == 274:

        # Right
        elif event.key == 100 or event.key == 275:
            self.state = 1


    def draw(self):
        if self.state == 0:
            self.screen.blit(self.leftImage, self.drawRect)
        elif self.state == 1:
            self.screen.blit(self.rightImage, self.drawRect)

#Enemy class
class Enemies(GameObject):

    TRICERATOPS = 0
    APATOSAURUS = 1
    TREX = 2
    RAPTOR = 3

    def __init__(self, screen, boardX, boardY, enemyType = 0):
        GameObject.__init__(self, screen, boardX, boardY)
        self.type = enemyType

        #Load the enemy based on the type

    def get_type(self):
        return self.type

    def draw(self):
        #wil totally draw stuff later
        return

#available munchables
class Munchables:
    #Types of munchables

    #Angles
    ANGLE_ACUTE = 0
    ANGLE_RIGHT = 1
    ANGLE_OBTUSE = 2

    #Triangles
    TRIANGLE_EQUILATERAL = 3
    TRIANGLE_ISOSCELES = 4
    TRIANGLE_SCALENE = 5
    TRIANGLE_RIGHT = 6

    #Quadrilaterals
    QUAD_SQUARE = 7
    QUAD_RECTANGLE = 8
    QUAD_TRAPEZOID = 9
    QUAD_PARALLELOGRAMS = 10
    QUAD_CONVEX = 11
    QUAD_CONCAVE = 12

    #Regular Polygons
    REGULAR_PENTAGON = 13
    REGULAR_HEXAGON = 14
    REGULAR_HEPTAGON = 15
    REGULAR_OCTAGON = 16
    REGULAR_NONAGON = 17
    REGULAR_DECAGON = 18
    REGULAR_HENDECAGON = 19
    REGULAR_DODECAGON = 20

    #Irregular Convex Polygons
    CONVEX_PENTAGON = 21
    CONVEX_HEXAGON = 22
    CONVEX_HEPTAGON = 23
    CONVEX_OCTAGON = 24
    CONVEX_NONAGON = 25
    CONVEX_DECAGON = 26
    CONVEX_HENDECAGON = 27
    CONVEX_DODECAGON = 28

    #Irregular Concave Polygons
    CONCAVE_PENTAGON = 29
    CONCAVE_HEXAGON = 30
    CONCAVE_HEPTAGON = 31
    CONCAVE_OCTAGON = 32
    CONCAVE_NONAGON = 33
    CONCAVE_DECAGON = 34
    CONCAVE_HENDECAGON = 35
    CONCAVE_DODECAGON = 36


    def __init__(self, screen, boardX, boardY, munchableType = 0):
        GameObject.__init__(self, screen, boardX, boardY)
        self.type = munchableType

        #Load image based on type

    def draw(self):
        #definitely does stuff
        return
