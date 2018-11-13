import pygame
import time
import random

pygame.display.init()
pygame.font.init()
screen_height = 1600
screen_width = 900
screen = pygame.display.set_mode([screen_height, screen_width])
pygame.display.set_caption("Boink")

#Images
background = pygame.image.load("background.jpg").convert()
credits_screen = pygame.image.load("credits_screen.png").convert()

#Class Definitions
class Character:
      x = 50
      y = 50
      width = 60
      height = 80
      vel = 1

class Enemy:
      pass

#Function Definitions
def load_image(image):
      screen.blit(image, (0, 0))


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

      #Creates a list of all keys
      keys = pygame.key.get_pressed()

      #If "E" key is pressed display e_image
      if keys[pygame.K_TAB]:
            load_image(credits_screen)
      
      #The display update should be at the end of the code            
      pygame.display.update()

pygame.quit()

      
      
