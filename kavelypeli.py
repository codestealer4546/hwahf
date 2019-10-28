import pygame
import sys
pygame.init()

koko = (600, 600)
naytto = pygame.display.set_mode(koko)

pelaaja = pygame.image.load("sprite.png")
musta = (0, 0, 0)
koordinaatit = [0, 0]

while True:
    naytto.fill(musta)
    naytto.blit(pelaaja, koordinaatit)
    pygame.display.flip()

    tapahtumat = pygame.event.get()
    for tapahtuma in tapahtumat:
        if tapahtuma.type == pygame.QUIT: # sulkee ikkunan
            sys.exit()
        # liikkuminen WASD
        elif tapahtuma.type == pygame.KEYDOWN:
            if tapahtuma.key == pygame.K_w:
                koordinaatit[1] = koordinaatit[1] - 10
            elif tapahtuma.key == pygame.K_s:
                koordinaatit[1] = koordinaatit[1] + 10
            elif tapahtuma.key == pygame.K_a:
                koordinaatit[0] = koordinaatit[0] - 10
            elif tapahtuma.key == pygame.K_d:
                koordinaatit[0] = koordinaatit[0] + 10

            # että et voi mennä pois ruudulta
            if koordinaatit[0] < 0:
                koordinaatit[0] = 0
            if koordinaatit[1] < 0:
                koordinaatit[1] = 0
            
            # että et voi mennä pois ruudulta
            if koordinaatit[0] > koko:
                koordinaatit[0] = 0
            if koordinaatit[1] > koko:
                koordinaatit[1] = 0                        