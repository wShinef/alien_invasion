import sys

import pygame

pygame.init()
screen = pygame.display.set_mode((1024, 768))
pygame.display.set_caption("test")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
screen.fill((255, 255, 255))
pygame.display.flip()
