import pygame, sys
from pygame.locals import QUIT
import Constants
import levels
from menu import *

class arrow:
    def __init__(self, WINDOW, level, x, y, goto, angle = 0):
        self.WINDOW = WINDOW
        self.level = level
        self.x = x
        self.arrow_raw = pygame.image.load("./Objects_Level_3/arrow.png")
        self.arrow_raw = pygame.transform.scale(self.arrow_raw, (100, 100))
        self.arrow = pygame.transform.rotate(self.arrow_raw, angle)
        self.rect = self.arrow.get_rect()
        self.rect.x = self.x
        self.y = y
        self.rect.y = self.y
        self.colliding = False
        #self.WINDOW.blit(self.arrow, (self.x, self.y))
        self.goto = goto
        #pygame.display.update()

    def check_collision(self, mouse_pos):
        self.colliding = self.rect.collidepoint(mouse_pos)
        return self.colliding
    def whenClicked(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    print("Clicked arrow")
                    return True

    def render(self, screen):
        screen.blit(self.arrow, (self.x, self.y))
