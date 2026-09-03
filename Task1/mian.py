import sys
import pygame
import random

# pygame setup
width, height = 1280, 720
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Floppy Ball")
clock = pygame.time.Clock()

#ball setup
ball_x = 80
ball_y = height // 2
ball_radius = 20
ball_velocity = 0
gravity = 0.5
flap_strength = -10

#pipe setup
pipe_width = 80
pipe_gap = 200
pipe_x = width
pipe_gap_y = 250
pipe_speed = 3
pipe_list = []
spawn_interval = 1500
last_spawn_time = pygame.time.get_ticks()


def create_pipe():
    gap_y = random.randint(100, height - 100 - pipe_gap)
    return {"x": width, "gap_y": gap_y, "scored": False}

score = 0

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
                    score = 0
                    pipe_list.clear()
                elif state == "playing":
                    ball_velocity = flap_strength

    if state == "playing":
        ball_velocity += gravity
        ball_y += ball_velocity

        if ball_x < width // 3:
            ball_x += 3
        if ball_x > width // 3:
            ball_x = width // 3


        #spawn pipes
        current_time = pygame.time.get_ticks()
        if current_time - last_spawn_time > spawn_interval:
            pipe_gap_y = random.randint(100, height - 100 - pipe_gap)
            pipe_list.append({"x": width, "gap_y": pipe_gap_y, "scored": False})
            last_spawn_time = current_time

        for pipe in pipe_list:
            pipe["x"] -= pipe_speed
            if pipe["x"] + pipe_width < 0:
                pipe["x"] = width
                pipe["gap_y"] = random.randint(100, height - 100 - pipe_gap)
                pipe["scored"] = False

        #collision detection
        for pipe in pipe_list:
            if (ball_x + ball_radius > pipe["x"] and ball_x - ball_radius < pipe["x"] + pipe_width):
                if (ball_y - ball_radius < pipe["gap_y"] or ball_y + ball_radius > pipe["gap_y"] + pipe_gap):
                    state = "game_over"
                    

            #score detection
            if not pipe["scored"] and ball_x > pipe["x"] + pipe_width:
                score += 1
                pipe["scored"] = True

        if ball_y - ball_radius <= 0 or ball_y + ball_radius > height:
          state = "game_over"


    # Draw everything

    screen.fill((135, 206, 235))
    pygame.draw.circle(screen, (255, 0, 0), (ball_x, ball_y), ball_radius) 

    
    for pipe in pipe_list:
        pygame.draw.rect(screen, (0, 255, 0), (pipe["x"], 0, pipe_width, pipe["gap_y"]))
        pygame.draw.rect(screen, (0, 255, 0), (pipe["x"], pipe["gap_y"] + pipe_gap, pipe_width, height - (pipe["gap_y"] + pipe_gap))) 
    

    score_font = pygame.font.Font(None, 36)
    score_text = score_font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))


    font = pygame.font.Font(None, 74)    

    if state == "game_over":
        text = font.render(f"Game Over Score: {score}", True, (255, 255, 255))
    if state == "start":
        text = font.render("Press SPACE to start", True, (255, 255, 255))

    if state in ["start", "game_over"]:
      text_rect = text.get_rect(center=(width // 2, height // 2))
      screen.blit(text, text_rect)

    pygame.display.flip() 
    dt = clock.tick(60)

pygame.quit()
sys.exit()