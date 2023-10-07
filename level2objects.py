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
    self.box = pygame.transform.scale(self.box, (100,100))
    self.rect = pygame.Rect(self.x + 100,200,250,200)
    self.y = y

    self.colliding = False
    self.WINDOW.blit(self.box, (self.x,self.y))

  def check_collision(self, mouse_pos):
    self.colliding = self.rect.collidepoint(mouse_pos)
    return self.colliding

  def whenClicked(self):
    pass

class openbox():
  def __init__(self, WINDOW,level,x=380,y=60):
    self.WINDOW = WINDOW
    self.level = level
    self.x = x
    self.box = pygame.image.load("./Objects_Level_2/openbox.png")
    self.box = pygame.transform.scale(self.box, (400,400))
    self.rect = pygame.Rect(self.x + 100,200,250,200)
    self.y = y
    self.colliding = False
    self.WINDOW.blit(self.box, (self.x,self.y))

  def check_collision(self, mouse_pos):
    self.colliding = self.rect.collidepoint(mouse_pos)
    return self.colliding

  def whenClicked(self):
    pass

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
