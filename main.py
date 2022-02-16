import pygame

pygame.init()  # Start pygame functions

COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_RED = (255, 0, 0)
COLOR_GREEN = (0, 255, 0)
COLOR_BLUE = (0, 0, 255)
COLOR_YELLOW = (255, 255, 0)
COLOR_ORANGE = (255, 125, 0)

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
screen.blit(frame, (10, 10))

# player
player = pygame.image.load("assets/player.png")  # player sprite
player_x = 225  # player X position
player_move_right = False  # player's initial movement condition
player_move_left = False  #

# ball
ball = pygame.image.load("assets/ball.png")
ball_x = 245
ball_y = 300
ball_dx = 5
ball_dy = 5

# hud
score_1_font = pygame.font.Font('assets/Square.ttf', 44)  # score
score_1_text = score_1_font.render('000', True, COLOR_WHITE, COLOR_BLACK)
score_1_text_rect = score_1_text.get_rect()
score_1_text_rect.center = (100, 100)

attempt_1_font = pygame.font.Font('assets/Square.ttf', 44)  # score
attempt_1_text = attempt_1_font.render('1', True, COLOR_WHITE, COLOR_BLACK)
attempt_1_text_rect = attempt_1_text.get_rect()
attempt_1_text_rect.center = (50, 55)

score_2_font = pygame.font.Font('assets/Square.ttf', 44)  # score
score_2_text = score_2_font.render('000', True, COLOR_WHITE, COLOR_BLACK)
score_2_text_rect = score_2_text.get_rect()
score_2_text_rect.center = (350, 100)

attempt_2_font = pygame.font.Font('assets/Square.ttf', 44)  # score
attempt_2_text = attempt_2_font.render('1', True, COLOR_WHITE, COLOR_BLACK)
attempt_2_text_rect = attempt_2_text.get_rect()
attempt_2_text_rect.center = (300, 55)

# score
score = 0

while game_loop:

    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False

    # drawing objects
    screen.blit(score_1_text, score_1_text_rect)
    screen.blit(score_2_text, score_2_text_rect)
    screen.blit(attempt_1_text, attempt_1_text_rect)
    screen.blit(attempt_2_text, attempt_2_text_rect)

    # update screen
    pygame.display.flip()  # screen update
    game_clock.tick(60)

pygame.quit()
