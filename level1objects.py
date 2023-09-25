import pygame, sys
from pygame.locals import QUIT
import Constants
import levels
from menu import *
class Bed():
  def __init__(self, WINDOW,level,x=380,y=60):
    self.WINDOW = WINDOW
    self.level = level
    self.x = x
    self.bed = pygame.image.load("./Objects_Level_1/bed.png")
    self.bed = pygame.transform.scale(self.bed, (400,400))
    self.rect = pygame.Rect(self.x + 100,200,250,200)
    self.y = y

    self.colliding = False
    self.WINDOW.blit(self.bed, (self.x,self.y))

  def check_collision(self, mouse_pos):
    self.colliding = self.rect.collidepoint(mouse_pos)
    return self.colliding

  def whenClicked(self):
    if self.check_collision(pygame.mouse.get_pos()):
      self.level.movebed(self.WINDOW)
      pygame.display.update()
class Toilet():
  def __init__(self, WINDOW):
    self.WINDOW = WINDOW
    self.x = 10
    self.toilet = pygame.image.load("./Objects_Level_1/toilet.png")
    self.toilet1 = pygame.image.load("./Objects_Level_1/opentoilet.png")
    self.toilet = pygame.transform.scale(self.toilet, (300,300))
    self.toilet1 = pygame.transform.scale(self.toilet1, (300, 300))
    self.rect = pygame.Rect(self.x + 100, 200, 250, 200)
    self.open = False

    self.WINDOW.blit(self.toilet, (10,160))
    pygame.display.update()

  def check_collision(self, mouse_pos):
    self.colliding = self.rect.collidepoint(mouse_pos)
    return self.colliding

  def whenClicked(self):
    if self.check_collision(pygame.mouse.get_pos()):
      self.WINDOW.blit(self.toilet1, (10, 160))
      self.open = True
      pygame.display.update()
    
class Key():
  def __init__(self, WINDOW):

    self.x=10

    self.rect = pygame.Rect(self.x + 120, 300, 50, 50)
    self.WINDOW = WINDOW
    self.key = pygame.image.load("./Objects_Level_1/key.png")
  def whenClicked(self):
    if self.check_collision(pygame.mouse.get_pos()):
      self.WINDOW.fill(Constants.WHITE)
      main_menu_obj = Main_menu(self.WINDOW)
      main_menu_obj.main_menu()

  def check_collision(self, mouse_pos):
    self.colliding = self.rect.collidepoint(mouse_pos)
    return self.colliding
  def checkToilet(self, Toilet):
    if Toilet.open == True:
      self.WINDOW.blit(self.key, (140, 305))
      pygame.display.update()
