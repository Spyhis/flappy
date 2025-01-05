import pygame
import os

class Gameover(pygame.sprite.Sprite):
    def __init__(self, *groups):
        self.image = pygame.image.load(os.path.join("images","gameover.png"))
        self.rect = self.image.get_rect(topleft= (50, 100))

        super().__init__(*groups)