import pygame

#player class
class Player:

    def __init__(self, screen):
        self.x = 0
        self.y = 0
        self.points = 0

        self.screen = screen

        self.leftImage = pygame.image.load("res/img/PlayerLeft.png")
        self.rightImage = pygame.image.load("res/img/PlayerRight.png")

        self.width = self.leftImage.get_width()
        self.height = self.leftImage.get_height()

        self.rect = (self.x, self.y, self.width, self.height)

        # State for which way to face; 0 is left, 1 is right
        self.state = 0

    def get_position(self):
        return self.x, self.y

    def get_points(self):
        return self.points

    def set_position(self, x, y):
        self.x = x
        self.y = y

        self.rect = (self.x, self.y, self.width, self.height)

    def add_points(self, points):
        self.points += points

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
            self.screen.blit(self.leftImage, self.rect)
        elif self.state == 1:
            self.screen.blit(self.rightImage, self.rect)

#list of enemies
class Enemies:

    PIRATE = 1
    DINOSAUR = 2

    def __init__(self):
        self.type = self.PIRATE
        self.x = 0
        self.y = 0

    def update(self, x, y):
        self.x = x
        self.y = y

    def type(self):
        return self.type


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
