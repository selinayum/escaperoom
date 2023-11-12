import pygame, sys
from pygame.locals import QUIT
import Constants
import levels
from menu import *

class Arrow:
    def __init__(self, WINDOW, level, open=False):
        self.WINDOW = WINDOW
        self.level = level
        self.x =
        self.arrow = pygame.image.load("./Objects_Level_3/arrow.png")

        self.arrow = pygame.transform.scale(self.arrow, (100, 100))

        self.y = 300
        self.colliding = False
        self.WINDOW.blit(self.box, (self.x, self.y))
        if open:
            self.WINDOW.blit(self.openbox, (self.x - 21, self.y - 6))
            self.open = True
            pygame.display.update()

        def check_collision(self, mouse_pos):
            self.colliding = self.rect.collidepoint(mouse_pos)
            return self.colliding


        def whenClicked(self, ghost):
            if ghost.visibility == True:
                return
            if self.check_collision(pygame.mouse.get_pos()) and self.open == False:
                pygame.draw.rect(self.WINDOW, Constants.WHITE, pygame.Rect(250, 100, 250, 200))
                    self.WINDOW.blit(self.openbox, (self.x - 21, self.y - 6))
                    self.open = True
                self.level.setUpLevel2()
                pygame.display.update()
