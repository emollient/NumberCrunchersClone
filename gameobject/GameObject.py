#player class
import pygame
class Player(pygame.sprite.Sprite):

    def __init__(self):
        self.x = 0
        self.y = 0
        self.points = 0

    def position(self):
        return self.x, self.y

    def points(self):
        return self.points

    def update(self, x, y, points=0):
        self.x = x
        self.y = y
        self.points+= points

    def draw(self):
        #definitely does stuff
        return

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

    def draw(self):
        #definitely does stuff
        return


#available munchables
class Munchables:
    #put the types of munchables here


    def __init__(self, x, y):
        self.x = x
        self.y = y
        return self.x, self.y
<<<<<<< HEAD

    def draw(self):
        #definitely does stuff
        return


=======
>>>>>>> 992176e4befbf52c4c203468f7d1186ec50fef26
