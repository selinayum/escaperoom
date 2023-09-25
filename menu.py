import pygame, sys
from pygame.locals import QUIT
import Constants
import levels
class Main_menu():

  def __init__(self,WINDOW):
    self.currentLevel = 0
    self.playing = False
    self.WINDOW = WINDOW
  def main_menu(self):

    self.displayText(self.WINDOW, "Choose Your Level", 50, 30,
                     Constants.TEXT_COLOR)
    self.displayText(self.WINDOW, "(Press 1, 2 or 3)", 95, 15,
                     Constants.TEXT_COLOR)
    self.displayText(self.WINDOW, "1) Level 1", 160, 20,
                     Constants.TEXT_COLOR)
    self.displayText(self.WINDOW, "2) Level 2", 235, 20,
                     Constants.TEXT_COLOR)
    self.displayText(self.WINDOW, "3) Level 3", 310, 20,
                     Constants.TEXT_COLOR)
    pygame.display.update()
    Constants.fpsClock.tick(Constants.FPS)

    for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.KEYDOWN:
        if event.unicode == "1":
          level1 = levels.LVL1(self.WINDOW)
          self.currentLevel = 1
          self.playing = True

        if event.unicode == "2":
          level2 = levels.LVL2(self.WINDOW)
          print("2")
          self.currentLevel = 2
        if event.unicode == "3":
          level3 = levels.LVL3(self.WINDOW)
          print("3")
          self.currentLevel = 3

  def displayText(self, screen, msg, y, size, color):
    font = pygame.font.Font("font.ttf", size + 10)
    text = font.render(msg, 1, color)
    text_rect = text.get_rect(center=(Constants.WIDTH / 2, y))
    screen.blit(text, text_rect)
    pygame.display.update()

    return text