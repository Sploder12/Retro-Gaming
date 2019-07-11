import pygame

import sys


pygame.init()

pygame.display.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption('goat')

while(True):
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("end")
    pygame.display.update()