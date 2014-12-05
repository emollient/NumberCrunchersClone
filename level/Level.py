from gameobject.GameObject import Munchable
import random

class Level:

    Levels = []

    def __init__(self, screen, goodMunchableTypes, badMunchableTypes, numOfGoodMunchables):
        self.screen = screen;

        self.goodMunchableTypes = goodMunchableTypes
        self.badMunchableTypes = badMunchableTypes
        self.numOfGoodMunchables = numOfGoodMunchables

        Level.Levels.append(self)

        self.index = len(Level.Levels) - 1

    #Generates and returns a list of munchables for the level
    #based on the given criteria
    #This assumes that there are 30 spaces to fill
    def generateMunchables(self):

        goodMunchablesCreated = 0
        munchables = []

        for x in range(0,6):
            for y in range(0, 5):
                shouldBeGood = random.randint(0,1)

                nextMunchable = None

                if goodMunchablesCreated < self.numOfGoodMunchables and shouldBeGood:
                    whichGood = random.randint(0,len(self.goodMunchableTypes) - 1)
                    goodType = self.goodMunchableTypes[whichGood]

                    nextMunchable = Munchable(self.screen, x, y, goodType)
                else:
                    whichBad = random.randint(0,len(self.badMunchableTypes) - 1)
                    badType = self.badMunchableTypes[whichBad]

                    nextMunchable = Munchable(self.screen, x, y, badType)

                munchables.append(nextMunchable)

        return munchables
