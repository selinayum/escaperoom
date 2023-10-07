import pygame, sys
from pygame.locals import QUIT
import Constants
import levels
from menu import *

class box():
  def __init__(self, WINDOW,level,x=-20,y=300):
    self.WINDOW = WINDOW
    self.level = level
    self.x = x
    self.box = pygame.image.load("./Objects_Level_2/box.png")
    self.openbox = pygame.image.load("./Objects_Level_2/openbox.png")
    self.box = pygame.transform.scale(self.box, (100,100))
    self.openbox = pygame.transform.scale(self.openbox, (100, 100))
    self.rect = pygame.Rect(self.x + 25,330,50,50)
    self.y = y
    self.open = False
    self.colliding = False
    self.WINDOW.blit(self.box, (self.x,self.y))

  def check_collision(self, mouse_pos):
    self.colliding = self.rect.collidepoint(mouse_pos)
    return self.colliding

  def whenClicked(self):
    if self.check_collision(pygame.mouse.get_pos()):
      self.WINDOW.blit(self.openbox, (self.x-21, self.y-6))
      self.open = True
      pygame.display.update()


class carpet():
  def __init__(self, WINDOW,level,x=275,y=320):
    self.WINDOW = WINDOW
    self.level = level
    self.x = x
    self.carpet = pygame.image.load("./Objects_Level_2/carpet.png")
    self.carpet = pygame.transform.scale(self.carpet, (200,200))
    self.rect = pygame.Rect(self.x + 100,200,250,200)
    self.y = y
    self.colliding = False
    self.WINDOW.blit(self.carpet, (self.x, self.y))


class ghost():
  def __init__(self, WINDOW,level,x=30,y=250):
    self.WINDOW = WINDOW
    self.level = level
    self.x = x
    self.ghost = pygame.image.load("./Objects_Level_2/ghost.png")
    self.ghost = pygame.transform.scale(self.ghost, (200,200))
    self.rect = pygame.Rect(self.x + 100,200,250,200)
    self.y = y
    self.colliding = False
    self.WINDOW.blit(self.ghost, (self.x, self.y))

class picture():
  def __init__(self, WINDOW,level,x=550,y=120):
    self.WINDOW = WINDOW
    self.level = level
    self.x = x
    self.picture = pygame.image.load("./Objects_Level_2/picture.png")
    self.picture = pygame.transform.scale(self.picture, (200,200))
    self.rect = pygame.Rect(self.x + 100,200,250,200)
    self.y = y
    self.colliding = False
    self.WINDOW.blit(self.picture, (self.x, self.y))

class scissors():
  def __init__(self, WINDOW,level,x=355,y=430):
    self.WINDOW = WINDOW
    self.level = level
    self.x = x
    self.scissors = pygame.image.load("./Objects_Level_2/scissors.png")
    self.scissors = pygame.transform.scale(self.scissors, (50,50))
    self.rect = pygame.Rect(self.x + 100,200,250,200)
    self.y = y
    self.colliding = False
    # self.WINDOW.blit(self.scissors, (self.x, self.y))

class spoon():
  def __init__(self, WINDOW,level,x=19,y=338):
    self.WINDOW = WINDOW
    self.level = level
    self.x = x
    self.spoon = pygame.image.load("./Objects_Level_2/spoon.png")
    self.spoon = pygame.transform.scale(self.spoon, (25,25))
    self.rect = pygame.Rect(self.x + 100,200,250,200)
    self.y = y
    self.colliding = False
    # self.WINDOW.blit(self.spoon, (self.x, self.y))
