import pygame, sys
from pygame.locals import QUIT
import Constants
import level1objects
import level2objects
import level3objects

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
            self.spoonObj.vis = False
          if self.scissorsObj.whenClicked(self.carpetObj):
            self.holding = "scissors"
            self.scissorsObj.vis = False
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
    self.WINDOW.fill(Constants.BG_COLOR)

    # Setup background
    self.bg_main = pygame.image.load("./bgs/bg3.png")
    self.bg_cave = pygame.image.load("./bgs/bg4.png")
    self.bg_well = pygame.image.load("./Objects_Level_3/well.png")
    self.bg_well2 = pygame.image.load("Objects_Level_3/drainwell.png")
    self.ancient_drawing1 = level3objects.ancient_drawing(self.WINDOW, 3, 275, 80,"Objects_Level_3/Ancient drawing 1.png", 1)
    self.ancient_drawing2 = level3objects.ancient_drawing(self.WINDOW, 3, 150, 200,"Objects_Level_3/Ancient drawing 2.png", -1)
    self.ancient_drawing3 = level3objects.ancient_drawing(self.WINDOW, 3, 400, 200,"Objects_Level_3/Ancient drawing 3.png", 1)
    self.state = "main"
    self.onlevel = True
    self.colorkey=[]
    self.correctcolorkey=["blue","brown","white","black", "red","green"]
    self.wellstate = 0
    """
    while self.onlevel:
      for event in pygame.event.get():
        if event.type == QUIT:
          pygame.quit()
          sys.exit()
      self.setUpLevel3(state=self.state)
      #pygame.display.update()
      Constants.fpsClock.tick(Constants.FPS)
    """
  
  def gameLoop(self):
    while self.onlevel:
      events = pygame.event.get()
      for event in events:
        if event.type == QUIT:
          pygame.quit()
          sys.exit()
      self.setUpLevel3(events, state=self.state)
      pygame.display.update()
      Constants.fpsClock.tick(Constants.FPS)

  def setUpLevel3(self, events, state = "main"):
    self.WINDOW.fill(Constants.BG_COLOR)
    if state == "main":
      self.WINDOW.blit(self.bg_main, (0, 0))
      #self.arrow_right = level3objects.arrow(self.WINDOW, 3, 650, 250, "main")
      #self.arrow_down = level3objects.arrow(self.WINDOW, 3, 325, 390, "cave", angle=-90)
      #self.arrow_left = level3objects.arrow(self.WINDOW, 3, 10, 250, "well", angle=180)
      arrows = [level3objects.arrow(self.WINDOW, 3, 650, 250, "main"), level3objects.arrow(self.WINDOW, 3, 325, 390, "cave", angle=-90), level3objects.arrow(self.WINDOW, 3, 10, 250, "well", angle=180)]
      for arrow in arrows:
        arrow.render(self.WINDOW)
        if arrow.whenClicked(events):
          self.state = arrow.goto
      self.ckeys = level3objects.Color_key(self.WINDOW,3)
      self.ckeys.render(self.WINDOW)
    if state == "cave":
      self.WINDOW.blit(self.bg_cave, (0, 0))
      self.arrow_up = level3objects.arrow(self.WINDOW, 3, 325, 10, "main", angle=90)
      self.ancient_drawing1.update(events)
      self.ancient_drawing2.update(events)
      self.ancient_drawing3.update(events)
      self.arrow_up.render(self.WINDOW)
      if self.arrow_up.whenClicked(events):
        self.state = self.arrow_up.goto
    if state == "well":
      self.WINDOW.fill([212, 169, 51])
      if self.wellstate == 0:
        self.WINDOW.blit(self.bg_well, (0, 0))
      elif self.wellstate == 1:
        self.WINDOW.blit(self.bg_well2,(0,0))
      self.arrow_rightback = level3objects.arrow(self.WINDOW, 3, 650, 250, "main")
      self.arrow_rightback.render(self.WINDOW)
      if self.arrow_rightback.whenClicked(events):
        self.state = self.arrow_rightback.goto
      self.bluebutton = level3objects.Color_button(self.WINDOW,3,600,200,Constants.BLUE)
      self.bluebutton.render(self.WINDOW)
      if self.bluebutton.whenClicked(events)==None:
        pass
      else:
        #print(self.bluebutton.whenClicked(events))
        if "blue" not in self.colorkey:
          self.colorkey.append("blue")
        print(self.colorkey)
      self.brownbutton = level3objects.Color_button(self.WINDOW, 3, 435, 50, Constants.BROWN)
      self.brownbutton.render(self.WINDOW)
      if self.brownbutton.whenClicked(events) == None:
        pass
      else:
        # print(self.bluebutton.whenClicked(events))
        if "brown" not in self.colorkey:
          self.colorkey.append("brown")
        print(self.colorkey)
      self.whitebutton = level3objects.Color_button(self.WINDOW, 3, 245, 50, Constants.WHITE)
      self.whitebutton.render(self.WINDOW)
      if self.whitebutton.whenClicked(events) == None:
        pass
      else:
        # print(self.bluebutton.whenClicked(events))
        if "white" not in self.colorkey:
          self.colorkey.append("white")
        print(self.colorkey)
      self.blackbutton = level3objects.Color_button(self.WINDOW, 3, 100, 200, Constants.BLACK)
      self.blackbutton.render(self.WINDOW)
      if self.blackbutton.whenClicked(events) == None:
        pass
      else:
        # print(self.bluebutton.whenClicked(events))
        if "black" not in self.colorkey:
          self.colorkey.append("black")
        print(self.colorkey)
      self.redbutton = level3objects.Color_button(self.WINDOW, 3, 245, 350, Constants.RED)
      self.redbutton.render(self.WINDOW)
      if self.redbutton.whenClicked(events) == None:
        pass
      else:
        # print(self.bluebutton.whenClicked(events))
        if "red" not in self.colorkey:
          self.colorkey.append("red")
        print(self.colorkey)
      self.greenbutton = level3objects.Color_button(self.WINDOW, 3, 435, 350, Constants.GREEN)
      self.greenbutton.render(self.WINDOW)
      if self.greenbutton.whenClicked(events) == None:
        pass
      else:
        # print(self.bluebutton.whenClicked(events))
        if "green" not in self.colorkey:
          self.colorkey.append("green")
        print(self.colorkey)

      if len(self.colorkey) == len(self.correctcolorkey):
        if self.colorkey == self.correctcolorkey and self.wellstate ==0:
          self.wellstate = 1
        else:

          self.colorkey=[]

