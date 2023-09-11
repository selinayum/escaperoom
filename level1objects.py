import pygame, sys
from pygame.locals import QUIT
import Constants
import levels

class Bed():
  def __init__(self, WINDOW):
    self.WINDOW = WINDOW
    self.x = 380
    self.bed = pygame.image.load("./Objects_Level_1/bed.png")
    self.bed = pygame.transform.scale(self.bed, (400,400))
    self.rect = pygame.Rect(self.x + 100,200,250,200)
    

    self.colliding = False
    self.WINDOW.blit(self.bed, (self.x,60))

  def check_collision(self, mouse_pos):
    self.colliding = self.rect.collidepoint(mouse_pos)
    return self.colliding

  def whenClicked():
    pass

class Toilet():
  def __init__(self, WINDOW):
    self.WINDOW = WINDOW
    self.toilet = pygame.image.load("./Objects_Level_1/toilet.png")
    self.toilet1 = pygame.image.load("./Objects_Level_1/opentoilet.png")
    self.toilet = pygame.transform.scale(self.toilet, (300,300))

    self.WINDOW.blit(self.toilet, (10,160))

  def whenClicked():
    pass
    
class Key():
  def __init__(self, WINDOW):
    self.WINDOW = WINDOW
    self.key = pygame.image.load("./Objects_Level_1/key.png")

  def whenClicked():
    pass