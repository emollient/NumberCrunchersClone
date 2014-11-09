#!/usr/bin/python
import pygame
import sys

from board import board

from gi.repository import Gtk

class Button:

    def __init__(self, screen, callback, x, y, width = 0, height = 0, imagePrefix = ""):
        self.screen = screen

        #State is an "enum"
        #0 is static, 1 is hovered, 2 is pressed, 3 is triggered (released after pressed while still hovered)
        self.state = 0

        if not imagePrefix == "":
            self.staticImage = pygame.image.load("res/img/" + imagePrefix + "Static.png")
            self.hoveredImage = pygame.image.load("res/img/" + imagePrefix + "Hover.png")
            self.pressedImage = pygame.image.load("res/img/" + imagePrefix + "Pressed.png")

            width = self.staticImage.get_width()
            height = self.staticImage.get_height()

        else:
            self.staticImage = None
            self.hoveredImage = None
            self.pressedImage = None

        halfWidth = width / 2
        halfHeight = height / 2

        self.rect = (x - halfWidth, y - halfHeight, width , height)

        self.staticColor = (255,0,0)
        self.hoveredColor = (0,255,0)
        self.pressedColor = (0,0,255)

        self.wasPressed = False

        self.callback = callback

    def events(self, event):
        pos = event.pos
        button = 0

        if event.type == pygame.MOUSEBUTTONDOWN:
            button = event.button

        if pos[0] > self.rect[0] and pos[0] < self.rect[0] + self.rect[2] and pos[1] > self.rect[1] and pos[1] < self.rect[1] + self.rect[3]:
            self.state = 1 #Hovered
            if button == 1:
                self.state = 2 #Pressed
                self.wasPressed = True
            elif self.wasPressed and event.type == pygame.MOUSEBUTTONUP:
                self.callback()
        else:
            self.state = 0 #Static

    def draw(self):
        #We can't use a switch on the button state, but we can do a set of if/else statements
        if self.state == 0:
            if self.staticImage:
                self.screen.blit(self.staticImage, self.rect)
            else:
                pygame.draw.rect(self.screen, self.staticColor, self.rect)
        elif self.state == 1:
            if self.hoveredImage:
                self.screen.blit(self.hoveredImage, self.rect)
            else:
                pygame.draw.rect(self.screen, self.hoveredColor, self.rect)
        elif self.state == 2:
            if self.pressedImage:
                self.screen.blit(self.pressedImage, self.rect)
            else:
                pygame.draw.rect(self.screen, self.pressedColor, self.rect)

class Menu:

    def __init__(self, screen):
        self.screen = screen

        screenWidthHalf = screen.get_width()/2
        screenHeightHalf = screen.get_height()/2

        startButton = Button(screen, self.startGame, screenWidthHalf, screenHeightHalf + 100, 0, 0, "StartGameButton")
        exitButton = Button(screen, self.exitGame, screenWidthHalf, screenHeightHalf + 200, 0, 0, "ExitGameButton")

        self.buttons = [startButton, exitButton]

    def startGame(self):
        NumberMunchersGame.gameState = 1
    def exitGame(self):
        pygame.quit()
        sys.exit()

    def events(self, event):
        for button in self.buttons:
            button.events(event)

    def draw(self):
        for button in self.buttons:
            button.draw()

class NumberMunchersGame:

    #Game state determines where we are in the game
    #0 is menu, 1 is game
    gameState = 0

    def __init__(self):
        # Set up a clock for managing the frame rate.
        self.clock = pygame.time.Clock()

        #Create the screen
        self.screen = pygame.display.get_surface()

        self.menu = Menu(self.screen)

        self.board = Board(60, self.screen.get_width(), self.screen.get_height(), self.screen)

        self.paused = False

    def set_paused(self, paused):
        self.paused = paused

    # Called to save the state of the game to the Journal.
    def write_file(self, file_path):
        pass

    # Called to load the state of the game from the Journal.
    def read_file(self, file_path):
        pass

    #Event handling and logic goes here
    def events(self):
        # Pump PyGame messages.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.VIDEORESIZE:
                pygame.display.set_mode(event.size, pygame.RESIZABLE)

            if NumberMunchersGame.gameState == 0:
                if event.type == pygame.MOUSEMOTION or event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
                    self.menu.events(event)

            elif NumberMunchersGame.gameState == 1:
                print "test"

    #Update logic goes here
    def update(self):
        # Move the ball
        if not self.paused:
            return

    #Rendering logic goes here
    def draw(self):
        # Clear Display
        self.screen.fill((255, 255, 255))  # 255 for white

        if NumberMunchersGame.gameState == 0:
            # Draw the menu
            self.menu.draw()

        elif NumberMunchersGame.gameState == 1:
            # Draw the ball
            # pygame.draw.circle(self.screen, (255, 0, 0), (100, 100), 100)
            board.draw();

        # Flip Display
        pygame.display.flip()

    # The main game loop.
    def run(self):
        self.running = True

        while self.running:
            # Pump GTK messages.
            while Gtk.events_pending():
                Gtk.main_iteration()

            #Handle events
            self.events()

            #Handle game logic
            self.update()

            #Handle rendering
            self.draw()

            # Try to stay at 30 FPS
            self.clock.tick(30)


# This function is called when the game is run directly from the command line:
# ./NumberMunchersGame.py
def main():
    pygame.init()
    pygame.display.set_mode((600, 480), pygame.RESIZABLE)
    game = NumberMunchersGame()
    game.run()

if __name__ == '__main__':
    main()