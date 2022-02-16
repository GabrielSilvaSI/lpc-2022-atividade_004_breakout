import pygame

BLACK = (0, 0, 0)


class Brick(pygame.sprite.Sprite):
    # This class corresponds to bricks

    def __init__(self, color, width, height):  # call the constructor with parameters
        super().__init__()

        self.image = pygame.Surface([width, height])  # brick width and height

        pygame.draw.rect(self.image, color, [0, 0, width, height])  # create a brick drawing

        self.rect = self.image.get_rect()
