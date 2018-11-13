import pygame
import time
import random

pygame.display.init()
pygame.font.init()
screen_height = 1600
screen_width = 900
screen = pygame.display.set_mode([screen_height, screen_width])
pygame.display.set_caption("Boink")
background = pygame.image.load("background.jpg").convert()

#Class Definitions
class Character:
      pass

class Enemy:
      pass

run = True
while run:
      #Restarts the loop every 1 milli second
      pygame.time.delay(1)
      
      #Adds the background.jpg as the background
      screen.blit(background, (0, 0))
      
      #If the "X" button is pressed the game will end
      for event in pygame.event.get():
            if event.type == pygame.QUIT:
                  pygame.quit()
      
      #The display update should be at the end of the code            
      pygame.display.update()

      
      
