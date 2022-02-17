import pygame
from brick import Brick

pygame.init()  # Start pygame functions

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 125, 0)

SCORE_MAX = 448

# window properties
size = (490, 580)  # Screen size (width, height)
screen = pygame.display.set_mode(size)  # Screen display mode
pygame.display.set_caption("Breakout")  # Frame title
img = pygame.image.load('assets/icon.png')  # Get icon image
pygame.display.set_icon(img)  # Set frame icon

# game loop
game_loop = True
game_clock = pygame.time.Clock()

# frame
frame = pygame.image.load("assets/frame.png")

# player
player = pygame.image.load("assets/player.png")  # player sprite
player_x = 200  # player X position
player_move_left = False  # player's initial movement condition
player_move_right = False

# ball
ball = pygame.image.load("assets/ball.png")
ball_x = 245
ball_y = 290
ball_dx = 2
ball_dy = 2

# bricks
sprites_list = pygame.sprite.Group()
brick_group = pygame.sprite.Group()
color_ord = (RED, RED, ORANGE, ORANGE, GREEN, GREEN, YELLOW, YELLOW)
for color_ind in range(8):
    for i in range(14):  # red bricks line 1
        brick = Brick(color_ord[color_ind], 28, 8)
        brick.rect.x = 22 + i * 32
        brick.rect.y = 122 + (color_ind * 11)
        sprites_list.add(brick)
        brick_group.add(brick)

# hud
score_1_font = pygame.font.Font('assets/Square.ttf', 44)  # score 1
score_1_text = score_1_font.render('000', True, WHITE, BLACK)
score_1_text_rect = score_1_text.get_rect()
score_1_text_rect.center = (100, 100)

attempt_1_font = pygame.font.Font('assets/Square.ttf', 44)  # attempt 1
attempt_1_text = attempt_1_font.render('1', True, WHITE, BLACK)
attempt_1_text_rect = attempt_1_text.get_rect()
attempt_1_text_rect.center = (50, 55)

score_2_font = pygame.font.Font('assets/Square.ttf', 44)  # score 2
score_2_text = score_2_font.render('000', True, WHITE, BLACK)
score_2_text_rect = score_2_text.get_rect()
score_2_text_rect.center = (350, 100)

attempt_2_font = pygame.font.Font('assets/Square.ttf', 44)  # attempt 2
attempt_2_text = attempt_2_font.render('1', True, WHITE, BLACK)
attempt_2_text_rect = attempt_2_text.get_rect()
attempt_2_text_rect.center = (300, 55)

# score
score = 0

# sound effects
paddle_sound = pygame.mixer.Sound('assets/paddle.wav')
wall_sound = pygame.mixer.Sound('assets/wall.wav')
brick_sound = pygame.mixer.Sound('assets/brick.wav')
miss_sound = pygame.mixer.Sound('assets/miss.wav')


while game_loop:
    # ball movement
    ball_x = ball_x + ball_dx
    ball_y = ball_y + ball_dy
    screen.fill(BLACK)

    # ball collision with the side walls
    if ball_x > 457:
        ball_dx *= -1
    elif ball_x <= 20:
        ball_dx *= -1

    # ball collision with the top and botton wall
    if ball_y >= 575:
        ball_dy *= -1
    if ball_y <= 28:
        ball_dy *= -1
    
                
    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False

        # paddle position
        mouse_x, mouse_y = pygame.mouse.get_pos()
        player_x = mouse_x

        # checking the victory condition
        if score < SCORE_MAX:
            # clear screen
            screen.fill(BLACK)
        
        # dellimiters 
        if player_x <= 20:
            player_x = 20
        elif player_x >= 430:
            player_x = 430

        # ball collision with the player's paddle
        if ball_y >= 525:
            if 525 <= ball_y + 10:
                if 525 + 20 > ball_y:
                    ball_dy *= -1


    # drawing objects
    screen.blit(frame, (10, 10))
    screen.blit(player, (player_x, 535))  # player (sprite, (X, Y))
    screen.blit(ball, (ball_x, ball_y))
    screen.blit(score_1_text, score_1_text_rect)
    screen.blit(score_2_text, score_2_text_rect)
    screen.blit(attempt_1_text, attempt_1_text_rect)
    screen.blit(attempt_2_text, attempt_2_text_rect)
    sprites_list.draw(screen)

    # update screen
    pygame.display.flip()  # screen update
    game_clock.tick(60)

pygame.quit()