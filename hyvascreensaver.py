import pygame
import sys
import random
pygame.init()

koko = (600, 600)
naytto = pygame.display.set_mode(koko)

kolikko = pygame.image.load("kolikko.png")
kolikko = pygame.transform.scale(kolikko, [64, 64])
koordinaatit = [0, 0]

while True:
    koordinaatit[0] = random.randint(0, 600)
    koordinaatit[1] = random.randint(0, 600)
    naytto.blit(kolikko, koordinaatit)

    tapahtumat = pygame.event.get()
    for tapahtuma in tapahtumat:
        if tapahtuma.type == pygame.QUIT: # sulkee ikkunan
            sys.exit()

        elif tapahtuma.type == pygame.MOUSEBUTTONDOWN:
            paikka = tapahtuma.pos
            print(paikka) 
            
    pygame.display.flip()