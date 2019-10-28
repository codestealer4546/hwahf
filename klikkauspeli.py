import pygame
import sys
import random
pygame.init()

koko = (600, 600)
naytto = pygame.display.set_mode(koko)

kolikko = pygame.image.load("kolikko.png")
kolikko = pygame.transform.scale(kolikko, [64, 64])
koordinaatit = [0, 0]

pisteet = 0

musta = (0, 0, 0)
sininen = (0, 0, 255)
punainen = (255, 0, 0)
keltainen = (255, 255, 0) 

while True:
    naytto.fill(musta)
    naytto.blit(kolikko, koordinaatit)
    

    tapahtumat = pygame.event.get()
    for tapahtuma in tapahtumat:
        if tapahtuma.type == pygame.QUIT: # sulkee ikkunan
            sys.exit()

        elif tapahtuma.type == pygame.MOUSEBUTTONDOWN:
            paikka = tapahtuma.pos

            if paikka[0] >= koordinaatit[0] and paikka[0] <= koordinaatit[0] + 64 and paikka[1] >= koordinaatit[1] and paikka[1] <= koordinaatit[1] + 64: 
                koordinaatit[0] = random.randint(0, koko[0])
                koordinaatit[1] = random.randint(0, koko[1])
                pisteet += 1
                print(pisteet)
            
    pygame.display.flip()