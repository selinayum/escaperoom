import pygame, sys
from pygame.locals import QUIT
import Constants
import levels
from menu import *

class box():
  def __init__(self, WINDOW,level, open = False):
    self.WINDOW = WINDOW
    self.level = level
    self.x = -20
    self.box = pygame.image.load("./Objects_Level_2/box.png")
    self.openbox = pygame.image.load("./Objects_Level_2/openbox.png")
    self.box = pygame.transform.scale(self.box, (100,100))
    self.openbox = pygame.transform.scale(self.openbox, (100, 100))
    self.rect = pygame.Rect(self.x + 25,330,50,50)
    self.y = 300
    self.open = open
    self.colliding = False
    self.WINDOW.blit(self.box, (self.x,self.y))
    if open:
      self.WINDOW.blit(self.openbox, (self.x - 21, self.y - 6))
      self.open = True
      pygame.display.update()

  def check_collision(self, mouse_pos):
    self.colliding = self.rect.collidepoint(mouse_pos)
    return self.colliding

  def displayText(self, screen, msg, y, size, color):
    font = pygame.font.Font("font.ttf", size + 30)
    text = font.render(msg, 1, color)
    text_rect = text.get_rect(center=(Constants.WIDTH / 2, y))
    screen.blit(text, text_rect)
    pygame.display.update()
  def whenClicked(self, ghost):
    if ghost.visibility == True:
      return
    if self.check_collision(pygame.mouse.get_pos()) and self.open == False:
      pygame.draw.rect(self.WINDOW,Constants.WHITE,pygame.Rect(250,100,250,200))
      self.displayText(self.WINDOW,"Enter Code:",140,14,Constants.TEXT_COLOR)
      codeentered=False
      code = ""
      while not codeentered and len(code)<4:
        for event in pygame.event.get():
          if event.type == pygame.KEYDOWN:
            if str(event.unicode) != "":
              print(event.unicode)
              code += event.unicode
              pygame.draw.rect(self.WINDOW, Constants.WHITE, pygame.Rect(250, 100, 250, 200))
              self.displayText(self.WINDOW, "Enter Code:", 140, 14, Constants.TEXT_COLOR)
              self.displayText(self.WINDOW,code,200,14,Constants.TEXT_COLOR)
      if code == "2839":
        self.WINDOW.blit(self.openbox, (self.x-21, self.y-6))
        self.open = True
      self.level.setUpLevel2()
      pygame.display.update()






class carpet():
  def __init__(self, WINDOW,level,x=275,y=320, moved = False):
    self.WINDOW = WINDOW
    self.level = level
    self.x = x
    self.carpet = pygame.image.load("./Objects_Level_2/carpet.png")
    self.carpet = pygame.transform.scale(self.carpet, (200,200))
    self.rect = pygame.Rect(self.x + 30,430,160,60)
    self.y = y
    self.colliding = False
    self.WINDOW.blit(self.carpet, (self.x, self.y))
    self.moved = moved

  def check_collision(self, mouse_pos):
    self.colliding = self.rect.collidepoint(mouse_pos)
    return self.colliding

  def whenClicked(self):
    if self.check_collision(pygame.mouse.get_pos()):
      self.level.setUpLevel2()
      self.moved = True
      pygame.display.update()



class ghost():
  def __init__(self, WINDOW,level,x=30,y=250, visibility = True):
    self.WINDOW = WINDOW
    self.level = level
    self.x = x
    self.ghost = pygame.image.load("./Objects_Level_2/ghost.png")
    self.ghost = pygame.transform.scale(self.ghost, (200,200))
    self.rect = pygame.Rect(self.x + 50,250,100,200)
    self.y = y
    self.colliding = False
    self.visibility = visibility
    if self.visibility:
      self.WINDOW.blit(self.ghost, (self.x, self.y))
  def whenClicked(self, hasscissors, scissorsobj):
    if self.check_collision(pygame.mouse.get_pos()) and hasscissors:
      self.visibility = False
      scissorsobj.visibility = True
      self.level.setUpLevel2()
      pygame.display.update()
  def check_collision(self, mouse_pos):
    self.colliding = self.rect.collidepoint(mouse_pos)
    return self.colliding
class picture():
  def __init__(self, WINDOW,level, moved = False):
    self.WINDOW = WINDOW
    self.level = level
    self.x = 550
    self.picture = pygame.image.load("./Objects_Level_2/picture.png")
    self.picture = pygame.transform.scale(self.picture, (200,200))
    self.rect = pygame.Rect(self.x+10,130,170,125)
    self.y = 120
    self.colliding = False
    self.WINDOW.blit(self.picture, (self.x, self.y))
    self.moved = moved
    if moved:
      pygame.draw.rect(self.WINDOW, (155, 146, 139), self.rect)
      self.displayText(self.WINDOW, "2839", 200, 12, Constants.TEXT_COLOR)
      pygame.display.update()

  def check_collision(self, mouse_pos):
    self.colliding = self.rect.collidepoint(mouse_pos)
    return self.colliding

  def displayText(self, screen, msg, y, size, color):
    font = pygame.font.Font("font.ttf", size + 30)
    text = font.render(msg, 1, color)
    text_rect = text.get_rect(center=(Constants.WIDTH / 2 + 270, y))
    screen.blit(text, text_rect)
    pygame.display.update()

    return text
  def whenClicked(self):
    if self.check_collision(pygame.mouse.get_pos()):
      self.moved = True
      pygame.draw.rect(self.WINDOW, (155, 146, 139), self.rect)
      self.displayText(self.WINDOW,"2839",200,12,Constants.TEXT_COLOR)
      pygame.display.update()




class scissors():
  def __init__(self, WINDOW,level,x=355,y=430, visibility = True):
    self.WINDOW = WINDOW
    self.level = level
    self.x = x
    self.scissors = pygame.image.load("./Objects_Level_2/scissors.png")
    self.scissors = pygame.transform.scale(self.scissors, (50,50))
    self.rect = pygame.Rect(self.x - 50,425,150,230)
    self.y = y
    self.colliding = False
    self.visibility = visibility

    # self.WINDOW.blit(self.scissors, (self.x, self.y))
    if self.visibility == False:
      self.displayText(self.WINDOW, "(Holding scissors)", 50, 12, Constants.TEXT_COLOR)



  def check_collision(self, mouse_pos):
    self.colliding = self.rect.collidepoint(mouse_pos)
    return self.colliding
  def displayText(self, screen, msg, y, size, color):
    font = pygame.font.Font("font.ttf", size + 30)
    text = font.render(msg, 1, color)
    text_rect = text.get_rect(center=(Constants.WIDTH / 2, y))
    screen.blit(text, text_rect)
    pygame.display.update()
  def whenClicked(self,carpet):
    if self.check_collision(pygame.mouse.get_pos()) and carpet.moved == True:
      self.displayText(self.WINDOW, "(Holding scissors)", 50, 12, Constants.TEXT_COLOR)
      return True


  def check_carpet(self,carpet):
    if carpet.moved == True and self.visibility == True:
      self.WINDOW.blit(self.scissors, (self.x, self.y))
      pygame.display.update


class spoon():
  def __init__(self, WINDOW,level,x=19,y=338):
    self.WINDOW = WINDOW
    self.level = level
    self.x = x
    self.spoon = pygame.image.load("./Objects_Level_2/spoon.png")
    self.spoon = pygame.transform.scale(self.spoon, (25,25))
    self.rect = pygame.Rect(self.x -15,330,50,50)
    self.y = y
    self.colliding = False
  def check_collision(self, mouse_pos):
    self.colliding = self.rect.collidepoint(mouse_pos)
    return self.colliding
  def whenClicked(self,box):
    if self.check_collision(pygame.mouse.get_pos()) and box.open == True:
      print("you have the spoon!")
      return True

  def check_box(self,box):
    if box.open == True:
      self.WINDOW.blit(self.spoon, (self.x, self.y))
      pygame.display.update

class flower():
  def __init__(self, WINDOW,level,x=300,y=270):
    self.WINDOW = WINDOW
    self.level = level
    self.x = x
    self.flower = pygame.image.load("./Objects_Level_2/flowerpot.PNG")
    self.flower = pygame.transform.scale(self.flower, (150,150))
    self.rect = pygame.Rect(self.x + 30,300,80,40)
    self.y = y
    self.colliding = False
    self.WINDOW.blit(self.flower, (self.x, self.y))

  def check_collision(self, mouse_pos):
    self.colliding = self.rect.collidepoint(mouse_pos)
    return self.colliding

  def whenClicked(self,Key, has_spoon):
    if self.check_collision(pygame.mouse.get_pos()):
      if Key.vis == False and has_spoon:
        Key.spawnKey()


class Key():
  def __init__(self, WINDOW):

    self.x=10

    self.rect = pygame.Rect(self.x + 340, 300, 50, 50)
    self.WINDOW = WINDOW
    self.key = pygame.image.load("./Objects_Level_1/key.png")
    self.vis = False

  def whenClicked(self):
    if self.check_collision(pygame.mouse.get_pos()) and self.vis:
      self.WINDOW.fill(Constants.WHITE)
      main_menu_obj = Main_menu(self.WINDOW)
      self.WINDOW.fill(Constants.BG_COLOR)
      main_menu_obj.main_menu()
      return True
    return False
  def check_collision(self, mouse_pos):
    self.colliding = self.rect.collidepoint(mouse_pos)
    return self.colliding
  def spawnKey(self):

    self.vis = True
    self.WINDOW.blit(self.key, (355, 305))
    pygame.display.update()
