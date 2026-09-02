import sys
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Floppy Ball")
clock = pygame.time.Clock()
running = True



while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((135, 206, 235))

    
    pygame.display.flip() 
    dt = clock.tick(60)

pygame.quit()