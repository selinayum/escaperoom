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

class ancient_drawing:
  def __init__(self, WINDOW, level, x, y, drawing, direction, moved = False):
    self.WINDOW = WINDOW
    self.level = level
    self.image = pygame.image.load(drawing)
    self.x = x
    self.y = y
    self.direction = direction
    self.image = pygame.transform.scale(self.image, (200, 200))
    self.colliding = False
    self.moved = moved
    self.rect = pygame.Rect(self.x+20, self.y+53, 160, 87)
    self.change_x = 0
    self.moving = False
    self.move_distance = self.x + 100 * self.direction


  def check_collision(self, mouse_pos):
    self.colliding = self.rect.collidepoint(mouse_pos)
    return self.colliding

  def whenClicked(self, events):
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.check_collision(pygame.mouse.get_pos()):
                print("picture was clicked")
                if self.x < self.move_distance:
                    self.moving = True


  def update(self, events):
      self.WINDOW.blit(self.image, (self.x, self.y))
      self.whenClicked(events)
      self.move()



  def displaytext(self, x, y, size, msg, color):
      font = pygame.font.Font("font.ttf", size + 30)
      text = font.render(msg, 1, color)
      pygame.display.update()

  def move(self):
      if self.moving == True:
          if self.x < self.move_distance and self.direction == 1:
              self.x += 1 * self.direction
              #self.x += self.change_x
          elif self.x > self.move_distance and self.direction == -1:
              self.x += 1 * self.direction

          else:
              self.moving = False




class Color_key:
    def __init__(self, WINDOW, level):
        self.WINDOW = WINDOW
        self.level = level
        self.x = 225
        self.y = 10
        self.colliding = False
        self.bluerect = [pygame.Rect(self.x, self.y, 50, 50),Constants.BLUE]
        self.brownrect = [pygame.Rect(self.x+50, self.y, 50, 50),Constants.BROWN]
        self.whiterect = [pygame.Rect(self.x + 100, self.y, 50, 50),Constants.WHITE]
        self.blackrect = [pygame.Rect(self.x + 150, self.y, 50, 50),Constants.BLACK]
        self.redrect = [pygame.Rect(self.x + 200, self.y, 50, 50),Constants.RED]
        self.greenrect = [pygame.Rect(self.x + 250, self.y, 50, 50),Constants.GREEN]
        self.colorrectlist = [self.bluerect,self.brownrect,self.whiterect,self.blackrect,self.redrect,self.greenrect]
    def render(self, screen):
        for rect in self.colorrectlist:
            pygame.draw.rect(screen,rect[1],rect[0])

class Color_button:
    def __init__(self,WINDOW,level,x,y,color):
        self.WINDOW = WINDOW
        self.level= level
        self.x = x
        self.y = y
        self.color = color
        self.rect = pygame.Rect(self.x,self.y,40,25)
    def render(self,screen):
        pygame.draw.rect(screen,self.color,self.rect)

    def check_collision(self, mouse_pos):
        self.colliding = self.rect.collidepoint(mouse_pos)
        return self.colliding

    def whenClicked(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.check_collision(pygame.mouse.get_pos()):
                    return self.color