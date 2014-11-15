import pygame

class GameObject:
    def __init__(self, screen, boardX, boardY):
        self.screen = screen

        self.screenRect = {'x':0, 'y':0, 'width':0, 'height':0}
        self.boardCoords = {'x':boardX, 'y':boardY}

        #More primitive datastructure for blitting to screen
        self.drawRect = None

    #update our drawRect object whenever the screenRect object is changed
    def update_drawRect(self):
        self.drawRect = (self.screenRect['x'], self.screenRect['y'], self.screenRect['width'], self.screenRect['height'])

    def get_boardCoords(self):
        return boardCoords

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
        if event.key == 119 or event.key == 273:
            print "up"

        # Left
        elif event.key == 97 or event.key == 276:
            self.state = 0

        # Down
        elif event.key == 115 or event.key == 274:
            print "down"

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

    TREX = 1
    APATASAUR = 2

    def __init__(self, screen, boardX, boardY, type = 1):
        GameObject.__init__(self, screen, boardX, boardY)
        self.type = self.TREX

        #Load the enemy based on the type

    def get_type(self):
        return self.type

    def draw(self):
        return 0



#available munchables
class Munchables:
    #put the types of munchables here

    def __init__(self, x, y):
        self.x = x
        self.y = y
        return self.x, self.y

    def draw(self):
        #definitely does stuff
        return
