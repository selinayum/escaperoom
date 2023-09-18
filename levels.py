import pygame, sys
from pygame.locals import QUIT
import Constants
import level1objects


class LVL1():

  def __init__(self, WINDOW):
    self.WINDOW = WINDOW
    self.WINDOW.fill(Constants.BG_COLOR)

    # Setup background
    self.bg = pygame.image.load("./bgs/bg1.png")
    self.WINDOW.blit(self.bg, (0, 0))

    # Load Objects
    self.bedObj = level1objects.Bed(self.WINDOW,self)
    self.toiletObj = level1objects.Toilet(self.WINDOW)
    self.keyObj = level1objects.Key(self.WINDOW)

    while True:
      for event in pygame.event.get():
        if event.type == QUIT:
          pygame.quit()
          sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
          self.bedObj.whenClicked()
      pygame.display.update()
      Constants.fpsClock.tick(Constants.FPS)

  def movebed(self, WINDOW):
    self.WINDOW = WINDOW
    self.WINDOW.fill(Constants.BG_COLOR)

    # Setup background
    self.bg = pygame.image.load("./bgs/bg1.png")
    self.WINDOW.blit(self.bg, (0, 0))

    # Load Objects
    self.bedObj = level1objects.Bed(self.WINDOW, self,380+60,60)
    self.toiletObj = level1objects.Toilet(self.WINDOW)
    self.keyObj = level1objects.Key(self.WINDOW)

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
