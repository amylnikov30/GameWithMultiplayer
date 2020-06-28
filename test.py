import pygame
import sys
import os


pygame.init()

fps = pygame.time.Clock()
window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("tests")





while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    

    window.fill((0, 34, 64))

    charlie = pygame.image.load('resource/img/models/masks/Charlie.png').convert()

    window.blit(charlie, (250, 250))

    pygame.display.update()
    fps.tick(200)
