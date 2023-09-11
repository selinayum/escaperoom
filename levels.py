import pygame, sys
from pygame.locals import QUIT
import Constants
import level1objects


class LVL1():

  def __init__(self, WINDOW):
    self.WINDOW = WINDOW

  def setUpLevel1(self):
    self.WINDOW.fill(Constants.BG_COLOR)

    # Setup background
    self.bg = pygame.image.load("./bgs/bg1.png")
    self.WINDOW.blit(self.bg, (0, 0))

    # Load Objects
    bedObj = level1objects.Bed(self.WINDOW)
    toiletObj = level1objects.Toilet(self.WINDOW)
    keyObj = level1objects.Key(self.WINDOW)


class LVL2():

  def __init__(self, WINDOW):
    self.WINDOW = WINDOW

  def setUpLevel2(self):
    self.WINDOW.fill(Constants.BG_COLOR)


class LVL3():

  def __init__(self, WINDOW):
    self.WINDOW = WINDOW

  def setUpLevel3(self):
    self.WINDOW.fill(Constants.BG_COLOR)
