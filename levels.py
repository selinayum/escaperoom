import pygame, sys
from pygame.locals import QUIT
import Constants
import level1objects
import level2objects

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
    self.onlevel = True

    while self.onlevel:
      for event in pygame.event.get():
        if event.type == QUIT:
          pygame.quit()
          sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
          if self.keyObj.whenClicked(self.toiletObj):
            self.onlevel = False
            self.WINDOW.fill(Constants.BG_COLOR)
            break
          self.bedObj.whenClicked()
          self.toiletObj.whenClicked()
          self.keyObj.checkToilet(self.toiletObj)
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
    self.WINDOW = WINDOW
    self.WINDOW.fill(Constants.BG_COLOR)

    # Setup background
    self.bg = pygame.image.load("./bgs/bg2.png")
    self.WINDOW.blit(self.bg, (0, 0))

  # Load Objects
    self.boxObj = level2objects.box(self.WINDOW,self)
    self.carpetObj = level2objects.carpet(self.WINDOW,self)
    self.ghostObj = level2objects.ghost(self.WINDOW,self)
    self.pictureObj = level2objects.picture(self.WINDOW,self)
    self.scissorsObj = level2objects.scissors(self.WINDOW,self)
    self.spoonObj = level2objects.spoon(self.WINDOW,self)
    self.flowerObj = level2objects.flower(self.WINDOW, self)
    self.KeyObj = level2objects.Key(self.WINDOW)
    self.onlevel = True
    self.holding = ""

    while self.onlevel:
      for event in pygame.event.get():
        if event.type == QUIT:
          pygame.quit()
          sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
          if self.KeyObj.whenClicked() == True and self.KeyObj.vis == True:
            self.onlevel=False
            self.spoonObj.vis = False
            self.scissorsObj.vis = False
            self.WINDOW.fill(Constants.BG_COLOR)
          if self.spoonObj.whenClicked(self.boxObj):
            self.holding = "spoon"
            self.spoonObj.visibility = False
          if self.scissorsObj.whenClicked(self.carpetObj):
            self.holding = "scissors"
            self.scissorsObj.visibility = False
            self.setUpLevel2()

          self.boxObj.whenClicked(self.ghostObj)
          self.flowerObj.whenClicked(self.KeyObj, self.holding == "spoon")
          self.carpetObj.whenClicked()
          self.pictureObj.whenClicked()
          self.ghostObj.whenClicked(self.holding == "scissors", self.scissorsObj)
          self.spoonObj.check_box(self.boxObj)
          self.scissorsObj.check_carpet(self.carpetObj)
      pygame.display.update()
      Constants.fpsClock.tick(Constants.FPS)


  def setUpLevel2(self):
    self.WINDOW.fill(Constants.BG_COLOR)
    self.bg = pygame.image.load("./bgs/bg2.png")
    self.WINDOW.blit(self.bg, (0, 0))

    # Load Objects
    self.boxObj = level2objects.box(self.WINDOW, self, self.boxObj.open)
    self.carpetObj = level2objects.carpet(self.WINDOW, self, 400, 320, True)
    self.ghostObj = level2objects.ghost(self.WINDOW, self, self.ghostObj.x, self.ghostObj.y, self.ghostObj.visibility)
    self.pictureObj = level2objects.picture(self.WINDOW, self, self.pictureObj.moved)
    self.scissorsObj = level2objects.scissors(self.WINDOW, self, self.scissorsObj.x, self.scissorsObj.y, self.scissorsObj.vis)
    self.spoonObj = level2objects.spoon(self.WINDOW, self)
    self.flowerObj = level2objects.flower(self.WINDOW, self)
class LVL3():

  def __init__(self, WINDOW):
    self.WINDOW = WINDOW

  def setUpLevel3(self):
    self.WINDOW.fill(Constants.BG_COLOR)
