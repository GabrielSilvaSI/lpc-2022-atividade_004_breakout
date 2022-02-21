import pygame

pygame.init()
pygame.mixer.init()

# dimensions
WIDTH = 890
HEIGHT = 750
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Breakout")
clock = pygame.time.Clock()
FPS = 60

# colors
WHITE = (255, 255, 255)
GREY = (212, 210, 212)
BLACK = (0, 0, 0)
BLUE = (0, 97, 148)
RED = (162, 8, 0)
ORANGE = (183, 119, 0)
GREEN = (0, 127, 33)
YELLOW = (197, 199, 37)

# components
score = 0
balls = 3
velocity = 4

# paddle
paddle_width = 54
paddle_height = 20

all_sprites_list = pygame.sprite.Group()

# all sounds
brick_sound = pygame.mixer.Sound("assets/brick.wav")
paddle_sound = pygame.mixer.Sound("assets/paddle.wav")
wall_sound = pygame.mixer.Sound("assets/wall.wav")
game_over_sound = pygame.mixer.Sound("assets/miss.wav")
loss_ball_sound = pygame.mixer.Sound("assets/lost_ball.mp3")


# class to build bricks
class Brick(pygame.sprite.Sprite):
    def __init__(self, color, width, height):  # call the constructor with parameters
        super().__init__()
        self.image = pygame.Surface([width, height])  # brick width and height
        pygame.draw.rect(
            self.image, color, [0, 0, width, height]
        )  # create a brick drawing
        self.rect = self.image.get_rect()


# class to build the paddle
class Paddle(pygame.sprite.Sprite):
    def __init__(self, color, width, height):  # call the constructor with parameters
        super().__init__()
        self.image = pygame.Surface([width, height])  # brick width and height
        pygame.draw.rect(
            self.image, color, [0, 0, width, height]
        )  # create a brick drawing
        self.rect = self.image.get_rect()

    def move_right(self, pixels):
        self.rect.x += pixels
        if self.rect.x > WIDTH - wall_width - paddle_width:
            self.rect.x = WIDTH - wall_width - paddle_width

    def move_left(self, pixels):
        self.rect.x -= pixels
        if self.rect.x < wall_width:
            self.rect.x = wall_width


# class to build the ball
class Ball(pygame.sprite.Sprite):
    def __init__(self, color, width, height):  # call the constructor with parameters
        super().__init__()
        self.image = pygame.Surface([width, height])  # brick width and height
        pygame.draw.rect(
            self.image, color, [0, 0, width, height]
        )  # create a brick drawing
        self.rect = self.image.get_rect()
        self.velocity = [velocity, velocity]

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity[0] = self.velocity[0]
        self.velocity[1] = -self.velocity[1]


# paddle construction
paddle = Paddle(BLUE, paddle_width, paddle_height)
paddle.rect.x = WIDTH // 2 - paddle_width // 2
paddle.rect.y = HEIGHT - 65

# ball construction
ball = Ball(WHITE, 10, 10)
ball.rect.x = WIDTH // 2 - 5
ball.rect.y = HEIGHT // 1.6 - 5

all_bricks = pygame.sprite.Group()

# dimensions of bricks
brick_width = 55
brick_height = 16
x_gap = 7
y_gap = 5
wall_width = 16


# construct bricks of different colors
def bricks():
    for j in range(9):
        for i in range(14):
            if j < 2:
                if i == 0:
                    brick = Brick(RED, brick_width, brick_height)
                    brick.rect.x = wall_width
                    brick.rect.y = 215 + j * (y_gap + brick_height)
                    all_sprites_list.add(brick)
                    all_bricks.add(brick)
                else:
                    brick = Brick(RED, brick_width, brick_height)
                    brick.rect.x = (
                            wall_width
                            + brick_width
                            + x_gap
                            + (i - 1) * (brick_width + x_gap)
                    )
                    brick.rect.y = 215 + j * (y_gap + brick_height)
                    all_sprites_list.add(brick)
                    all_bricks.add(brick)

            if 1 < j < 4:
                if i == 0:
                    brick = Brick(ORANGE, brick_width, brick_height)
                    brick.rect.x = wall_width
                    brick.rect.y = 215 + j * (y_gap + brick_height)
                    all_sprites_list.add(brick)
                    all_bricks.add(brick)
                else:
                    brick = Brick(ORANGE, brick_width, brick_height)
                    brick.rect.x = (
                            wall_width
                            + brick_width
                            + x_gap
                            + (i - 1) * (brick_width + x_gap)
                    )
                    brick.rect.y = 215 + j * (y_gap + brick_height)
                    all_sprites_list.add(brick)
                    all_bricks.add(brick)

            if 3 < j < 6:
                if i == 0:
                    brick = Brick(GREEN, brick_width, brick_height)
                    brick.rect.x = wall_width
                    brick.rect.y = 215 + j * (y_gap + brick_height)
                    all_sprites_list.add(brick)
                    all_bricks.add(brick)
                else:
                    brick = Brick(GREEN, brick_width, brick_height)
                    brick.rect.x = (
                            wall_width
                            + brick_width
                            + x_gap
                            + (i - 1) * (brick_width + x_gap)
                    )
                    brick.rect.y = 215 + j * (y_gap + brick_height)
                    all_sprites_list.add(brick)
                    all_bricks.add(brick)

            if 5 < j < 8:
                if i == 0:
                    brick = Brick(YELLOW, brick_width, brick_height)
                    brick.rect.x = wall_width
                    brick.rect.y = 215 + j * (y_gap + brick_height)
                    all_sprites_list.add(brick)
                    all_bricks.add(brick)
                else:
                    brick = Brick(YELLOW, brick_width, brick_height)
                    brick.rect.x = (
                            wall_width
                            + brick_width
                            + x_gap
                            + (i - 1) * (brick_width + x_gap)
                    )
                    brick.rect.y = 215 + j * (y_gap + brick_height)
                    all_sprites_list.add(brick)
                    all_bricks.add(brick)


bricks()
all_sprites_list.add(paddle)
all_sprites_list.add(ball)


# game-loop
def main(score_element, balls_element):
    step = 0
    run = True
    while run:
        # events on keyboard
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            paddle.move_left(10)

        if keys[pygame.K_RIGHT]:
            paddle.move_right(10)

        all_sprites_list.update()

        # collision with the walls
        if ball.rect.y < 40:
            ball.velocity[1] = -ball.velocity[1]
            wall_sound.play()

        if ball.rect.x >= WIDTH - wall_width - 10:
            ball.velocity[0] = -ball.velocity[0]
            wall_sound.play()

        if ball.rect.x <= wall_width:
            ball.velocity[0] = -ball.velocity[0]
            wall_sound.play()

        # collision with the bottom
        if ball.rect.y > HEIGHT:
            loss_ball_sound.play()
            ball.rect.x = WIDTH // 2 - 5
            ball.rect.y = HEIGHT // 1.6 - 5
            ball.velocity[1] = ball.velocity[1]
            balls_element -= 1
            # game-over
            if balls_element == 0:
                font = pygame.font.Font("assets/Square.ttf", 70)
                text = font.render("GAME OVER", 1, WHITE)
                text_rect = text.get_rect(center=(WIDTH / 2, HEIGHT / 1.5))
                screen.blit(text, text_rect)
                pygame.display.update()
                game_over_sound.play()
                pygame.time.wait(2000)
                run = False
        # collision with the paddle
        if pygame.sprite.collide_mask(ball, paddle):
            ball.rect.x += ball.velocity[0]
            ball.rect.y -= ball.velocity[1]
            ball.bounce()
            paddle_sound.play()

        # collision with the brick
        brick_collision_list = pygame.sprite.spritecollide(ball, all_bricks, False)
        for brick in brick_collision_list:
            ball.bounce()
            brick_sound.play()
            if len(brick_collision_list) > 0:
                step += 1
                for i in range(0, 488, 28):
                    if step == i:
                        ball.velocity[0] += 1
                        ball.velocity[1] += 1
            # brick punctuation
            if 380.5 > brick.rect.y > 338.5:
                score_element += 1
                brick.kill()
            elif 338.5 > brick.rect.y > 294:
                score_element += 3
                brick.kill()
            elif 294 > brick.rect.y > 254.5:
                score_element += 5
                brick.kill()
            else:
                score_element += 7
                brick.kill()
            # end-game
            if len(all_bricks) == 0:
                font = pygame.font.Font("assets/Square.ttf", 70)
                text = font.render("SCREEN CLEARED", 1, WHITE)
                text_rect = text.get_rect(center=(WIDTH / 2, HEIGHT / 2))
                screen.blit(text, text_rect)
                pygame.display.update()
                pygame.time.wait(2000)
                run = False

        screen.fill(BLACK)
        # Constructing delimiters
        pygame.draw.line(screen, GREY, [0, 19], [WIDTH, 19], 40)
        pygame.draw.line(
            screen,
            GREY,
            [(wall_width / 2) - 1, 0],
            [(wall_width / 2) - 1, HEIGHT],
            wall_width,
        )
        pygame.draw.line(
            screen,
            GREY,
            [(WIDTH - wall_width / 2) - 1, 0],
            [(WIDTH - wall_width / 2) - 1, HEIGHT],
            wall_width,
        )

        pygame.draw.line(
            screen,
            BLUE,
            [(wall_width / 2) - 1, HEIGHT - 65 + paddle_height / 2 - 54 / 2],
            [(wall_width / 2) - 1, HEIGHT - 65 + paddle_height / 2 - 54 / 2 + 54],
            wall_width,
        )

        pygame.draw.line(
            screen,
            BLUE,
            [(WIDTH - wall_width / 2) - 1, HEIGHT - 65 + paddle_height / 2 - 54 / 2],
            [
                (WIDTH - wall_width / 2) - 1,
                HEIGHT - 65 + paddle_height / 2 - 54 / 2 + 54,
            ],
            wall_width,
        )

        pygame.draw.line(
            screen,
            RED,
            [(wall_width / 2) - 1, 212.5],
            [(wall_width / 2) - 1, 212.5 + 2 * brick_height + 2 * y_gap],
            wall_width,
        )
        pygame.draw.line(
            screen,
            RED,
            [(WIDTH - wall_width / 2) - 1, 212.5],
            [(WIDTH - wall_width / 2) - 1, 212.5 + 2 * brick_height + 2 * y_gap],
            wall_width,
        )

        pygame.draw.line(
            screen,
            ORANGE,
            [(wall_width / 2) - 1, 212.5 + 2 * brick_height + 2 * y_gap],
            [(wall_width / 2) - 1, 212.5 + 4 * brick_height + 4 * y_gap],
            wall_width,
        )
        pygame.draw.line(
            screen,
            ORANGE,
            [(WIDTH - wall_width / 2) - 1, 212.5 + 2 * brick_height + 2 * y_gap],
            [(WIDTH - wall_width / 2) - 1, 212.5 + 4 * brick_height + 4 * y_gap],
            wall_width,
        )

        pygame.draw.line(
            screen,
            GREEN,
            [(wall_width / 2) - 1, 212.5 + 4 * brick_height + 4 * y_gap],
            [(wall_width / 2) - 1, 212.5 + 6 * brick_height + 6 * y_gap],
            wall_width,
        )
        pygame.draw.line(
            screen,
            GREEN,
            [(WIDTH - wall_width / 2) - 1, 212.5 + 4 * brick_height + 4 * y_gap],
            [(WIDTH - wall_width / 2) - 1, 212.5 + 6 * brick_height + 6 * y_gap],
            wall_width,
        )

        pygame.draw.line(
            screen,
            YELLOW,
            [(wall_width / 2) - 1, 212.5 + 6 * brick_height + 6 * y_gap],
            [(wall_width / 2) - 1, 212.5 + 8 * brick_height + 8 * y_gap],
            wall_width,
        )
        pygame.draw.line(
            screen,
            YELLOW,
            [(WIDTH - wall_width / 2) - 1, 212.5 + 6 * brick_height + 6 * y_gap],
            [(WIDTH - wall_width / 2) - 1, 212.5 + 8 * brick_height + 8 * y_gap],
            wall_width,
        )

        # score and count of lives
        font = pygame.font.Font("assets/Square.ttf", 70)
        text = font.render(str(f"{score_element:03}"), 1, WHITE)
        screen.blit(text, (80, 120))
        text = font.render(str(balls_element), 1, WHITE)
        screen.blit(text, (520, 41))
        text = font.render("000", 1, WHITE)
        screen.blit(text, (520, 120))
        text = font.render("1", 1, WHITE)
        screen.blit(text, (20, 40))

        all_sprites_list.draw(screen)

        pygame.display.update()

        clock.tick(FPS)

    pygame.quit()


main(score, balls)
