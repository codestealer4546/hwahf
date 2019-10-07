import pygame
import sys
pygame.init()

koko = (700, 600)
naytto = pygame.display.set_mode(koko)

musta = (0, 0, 0)
sininen = (0, 0, 255)
punainen = (255, 0, 0)
while True:
    naytto.fill(musta)
    pygame.draw.line(naytto, sininen, (150, 150), (300, 300), 10)
    pygame.draw.circle(naytto, punainen, (0, 0), (450, 450), 10)
    pygame.display.flip()

    # tarkistaa tapahtumia
    tapahtumat = pygame.event.get()
    for tapahtuma in tapahtumat:
        if tapahtuma.type == pygame.QUIT: # sulkee ikkunan
            sys.exit()