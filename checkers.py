import pygame
import sys

pygame.init()

#screen settings
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Checkers")

# colors
red = (255, 0, 0)
blue = (0, 0 , 255)
black =  (0, 0, 0)
white = (255, 255, 255)

