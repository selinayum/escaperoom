import pygame, sys
from pygame.locals import QUIT
import Constants
import levels
from menu import *

class Game():
  def __init__(self):
    self.WINDOW = pygame.display.set_mode((Constants.WIDTH, Constants.HEIGHT))
    pygame.display.set_caption('Escape Room')
    self.WINDOW.fill(Constants.BG_COLOR)
    pygame.init()

    self.playing = False
    self.currentLevel = 0
    
    while not self.playing:
      main_menu_obj = Main_menu(self.WINDOW)
      main_menu_obj.main_menu()

  def displayText(self, screen, msg, y, size, color):
    font = pygame.font.Font("font.ttf", size + 10)
    text = font.render(msg, 1, color)
    text_rect = text.get_rect(center=(Constants.WIDTH / 2, y))
    screen.blit(text, text_rect)
    pygame.display.update()

    return text


gameObj = Game()



