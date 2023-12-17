import pygame
import random

pygame.init()

screen_info = pygame.display.Info()
width, height = screen_info.current_w, screen_info.current_h
bg_color = (245, 245, 220)
screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)

dog_img = pygame.image.load('dog.png')
dog_rect = dog_img.get_rect()
dog_speed = 2
dog_x, dog_y = width // 2, height // 2

ball_img = pygame.image.load('ball.png')
ball_img = pygame.transform.scale(ball_img, (ball_img.get_width() // 2, ball_img.get_height() // 2))
ball_rect = ball_img.get_rect()
ball_speed = 0
balls = []

start_time = pygame.time.get_ticks()
game_time = 10000
time_increase_per_ball = 500
end_game_time = start_time + game_time

score = 0
font = pygame.font.Font(None, 36)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Gra z psem')

clock = pygame.time.Clock()
running = True

while running:
    screen.fill(bg_color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        dog_x -= dog_speed
    if keys[pygame.K_RIGHT]:
        dog_x += dog_speed
    if keys[pygame.K_UP]:
        dog_y -= dog_speed
    if keys[pygame.K_DOWN]:
        dog_y += dog_speed


    dog_rect.topleft = (dog_x, dog_y)


    if len(balls) < 1:
        ball_x = random.randint(0, width - ball_rect.width)
        ball_y = random.randint(0, height - ball_rect.height)
        ball_rect.topleft = (ball_x, ball_y)
        balls.append(ball_rect.copy())

    screen.blit(dog_img, dog_rect)

    for ball in balls[:]:
        screen.blit(ball_img, ball)

        if dog_rect.colliderect(ball):
            balls.remove(ball)
            score += 1
            game_time += time_increase_per_ball


    current_time = pygame.time.get_ticks()
    time_left = max(0, (end_game_time - current_time)) // 1000

    time_text = font.render(f'Czas: {time_left}', True, (0, 0, 0))
    screen.blit(time_text, (width // 2 - 50, 10))

    score_text = font.render(f'Złapane piłki: {score}', True, (0, 0, 0))
    screen.blit(score_text, (10, 50))

    if current_time >= end_game_time:
        running = False

    pygame.display.flip()


final_score_text = font.render(f'Zdobity wynik: {score}', True, (0, 0, 0))
text_rect = final_score_text.get_rect(center=(width // 2, height // 2))
screen.blit(final_score_text, text_rect)
pygame.display.flip()

pygame.time.wait(5000)
pygame.quit()