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

flap_strength = -10

state = "start" # "start", "playing", "game_over"

running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if state == "start":
                    ball_velocity = flap_strength
                    state = "playing"
                elif state == "game_over":
                    # Reset game state
                    state = "playing"
                    ball_y = height // 2
                    ball_velocity = 0
                    ball_x = 80
                    ball_velocity = flap_strength
                elif state == "playing":
                    ball_velocity = flap_strength

    if state == "playing":
        ball_velocity += gravity
        ball_y += ball_velocity

        if ball_x < width // 3:
            ball_x += 3
        if ball_x > width // 3:
            ball_x = width // 3

        if ball_y - ball_radius <= 0 or ball_y + ball_radius > height:
          state = "game_over"

    screen.fill((135, 206, 235))
    pygame.draw.circle(screen, (255, 0, 0), (ball_x, ball_y), ball_radius) 



    font = pygame.font.Font(None, 74)    

    if state == "game_over":
        text = font.render("Game Over", True, (255, 255, 255))
    if state == "start":
        text = font.render("Press SPACE to start", True, (255, 255, 255))

    if state in ["start", "game_over"]:
      text_rect = text.get_rect(center=(width // 2, height // 2))
      screen.blit(text, text_rect)

    pygame.display.flip() 
    dt = clock.tick(60)

pygame.quit()
sys.exit()