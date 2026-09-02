import sys
import pygame

# pygame setup
width, height = 1280, 720
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Floppy Ball")
clock = pygame.time.Clock()

ball_x = 80
ball_y = height // 2
ball_radius = 20
ball_velocity = 0
gravity = 0.5


running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    ball_velocity += gravity
    ball_y += ball_velocity

    screen.fill((135, 206, 235))
    pygame.draw.circle(screen, (255, 0, 0), (ball_x, ball_y), ball_radius)    
    pygame.display.flip() 
    dt = clock.tick(60)

pygame.quit()