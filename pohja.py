import pygame
import sys
pygame.init()

koko = (700, 600)
naytto = pygame.display.set_mode(koko)

musta = (0, 0, 0)
sininen = (0, 0, 255)
punainen = (255, 0, 0)

tapahtumat = pygame.event.get()
    for tapahtuma in tapahtumat:
        if tapahtuma.type == pygame.QUIT: # sulkee ikkunan
            sys.exit()